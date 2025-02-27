from itertools import islice

def lists_with_product_equal_n(circular_list):
    target_product = 415
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in islice(range(i, i + n), n):
            index = j % n
            num = circular_list[index]
            product *= num
            sublist.append(num)
            if product == target_product:
                result.append(sublist.copy())
            if product == 0 or product > target_product:
                break
    return result