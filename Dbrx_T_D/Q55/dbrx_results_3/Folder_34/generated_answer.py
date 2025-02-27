from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    target = -81
    result = []
    for i in range(len(numbers)):
        sub_product = 1
        sub_list = []
        for j in islice(cycle(numbers), i, len(numbers) + i):
            sub_product *= j
            sub_list.append(j)
            if sub_product == target:
                result.append(sub_list.copy())
                break
            elif sub_product < target:
                break
    return result