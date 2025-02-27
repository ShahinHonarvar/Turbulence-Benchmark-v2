from itertools import islice

def lists_with_product_equal_n(numbers):
    result = []
    n = 3
    for i in range(len(numbers)):
        sub_list = []
        product = 1
        for j in range(i, len(numbers) + i):
            current_number = numbers[j % len(numbers)]
            sub_list.append(current_number)
            product *= current_number
            if product == n:
                result.append(sub_list[:])
                break
            elif product > n:
                break
    return result