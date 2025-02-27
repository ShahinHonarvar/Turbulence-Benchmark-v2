from itertools import islice

def lists_with_product_equal_n(numbers, target=-32):
    result = []
    for i in range(len(numbers)):
        sublist = [numbers[i]]
        product = 1
        for j in range(len(numbers)):
            product *= numbers[j]
            if product == target:
                result.append(list(sublist))
                break
            elif product > target:
                break
            sublist.append(numbers[j])
    return result