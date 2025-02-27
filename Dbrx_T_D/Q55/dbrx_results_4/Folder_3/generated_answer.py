from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sub_result = []
        product = 1
        for j in range(i, len(lst) + i):
            num = lst[j % len(lst)]
            if num == 0 and product != 0:
                product = 0
                break
            if product == -22:
                break
            product *= num
            sub_result.append(num)
        if product == -22:
            result.append(sub_result)
    return result