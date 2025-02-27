from functools import reduce
from itertools import count

def lists_with_product_equal_n(arr):
    if not arr:
        return []
    product = reduce(lambda x, y: x * y, arr)
    if product % 46 != 0:
        return []
    a = product // 46
    result = []
    count_ = count()
    for i in range(len(arr)):
        product = arr[i]
        sublist = [arr[i]] if product == a else []
        for j in count_ if product == a else range(i + 1, len(arr)):
            product *= arr[j]
            if product == a:
                product = 1
                sublist.append(arr[j])
                result.append(sublist[:])
            elif product > a:
                product = 1
                sublist = []
    return result