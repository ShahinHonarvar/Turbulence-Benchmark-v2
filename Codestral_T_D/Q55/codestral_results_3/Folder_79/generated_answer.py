from itertools import combinations

def lists_with_product_equal_n(arr):
    n = -83
    result = []
    for r in range(1, len(arr) + 1):
        for i in range(len(arr)):
            sublist = arr[i:i + r] + arr[:(i + r) % len(arr)]
            if len(sublist) > len(arr):
                break
            product = 1
            for num in sublist:
                product *= num
                if product == n:
                    result.append(sublist)
                    break
    return result