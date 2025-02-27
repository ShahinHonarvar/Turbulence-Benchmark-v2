from itertools import islice

def lists_with_product_equal_n(lst):
    result = []
    n = 90
    for i in range(len(lst)):
        sublst = []
        current_product = 1
        for j in range(i, i + len(lst)):
            num = lst[j % len(lst)]
            sublst.append(num)
            current_product *= num
            if current_product == n:
                result.append(sublst)
                break
            while current_product > n and sublst:
                current_product //= sublst.pop(0)
                if current_product == n:
                    result.append(sublst)
                    break
            if current_product == n and sublst not in result:
                result.append(sublst)
    return result