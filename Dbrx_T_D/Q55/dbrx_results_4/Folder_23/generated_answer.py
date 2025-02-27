from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-95):
    result = []
    for i in range(len(numbers)):
        subproduct = 1
        sublist = []
        for j in islice(cycle(numbers), i, i + len(numbers)):
            subproduct *= j
            sublist.append(j)
            if subproduct == target:
                result.append(sublist)
            elif subproduct > target:
                break
    return result