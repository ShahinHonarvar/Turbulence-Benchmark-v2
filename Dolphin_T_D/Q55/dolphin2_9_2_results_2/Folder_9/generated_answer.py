from itertools import islice

def lists_with_product_equal_n(nums):
    n = len(nums)
    product = -36
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = list(islice(nums, i, j))
            if i > j - 2 and j < n or (i < j and j > n):
                continue
            if i == j - 2:
                result.append(sublist)
            else:
                prod = 1
                for k in sublist:
                    prod *= k
                if prod == product:
                    result.append(sublist)
    return result