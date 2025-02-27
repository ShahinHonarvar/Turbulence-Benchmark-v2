from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = -91
    result = []
    for i in range(len(numbers)):
        sub_list = []
        product = 1
        for num in islice(cycle(numbers), i, len(numbers) + i):
            if num == 0 and (not sub_list):
                break
            sub_list.append(num)
            product *= num
            if product == n:
                result.append(sub_list.copy())
                break
            elif product < n and (not sub_list):
                break
            elif product > n:
                break
    return result