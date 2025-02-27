from itertools import islice

def circular_slice(lst, start, size):
    length = len(lst)
    return lst[start:start + size] + [lst[i] for i in range(length - size, length) if i < (start + size) % length]

def lists_with_product_equal_n(lst, n):
    result, product, sublst = ([], 1, [])
    for i, num in enumerate(lst):
        if num != 0:
            sublst.append(num)
            product *= num
            while product < n and sublst:
                product //= sublst[0]
                sublst.pop(0)
            if product == n:
                result.append(sublst.copy())
                product //= sublst[0]
                sublst.pop(0)
        else:
            product = 1
            sublst = []
    for size in range(1, len(lst)):
        for i in range(len(lst) - size + 1):
            sublst = circular_slice(lst, i, size)
            product = 1
            for num in sublst:
                product *= num
            if product == n:
                sublst = list(sublst)
                if sublst not in result:
                    result.append(sublst)
    return result