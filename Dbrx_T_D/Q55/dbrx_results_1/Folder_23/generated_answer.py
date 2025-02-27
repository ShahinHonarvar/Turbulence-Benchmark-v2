from itertools import islice, cycle

def lists_with_product_equal_n(arr):
    if not arr:
        return []
    result = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarr = list(islice(cycle(arr), i, j + 1))
            if subarr:
                if subarr[0] == 0 and any((x != 0 for x in subarr[1:])):
                    result.append(subarr)
                elif prod(subarr) == -95:
                    result.append(subarr)
    return list(set(result))

def prod(arr):
    p = 1
    for num in arr:
        p *= num
    return p