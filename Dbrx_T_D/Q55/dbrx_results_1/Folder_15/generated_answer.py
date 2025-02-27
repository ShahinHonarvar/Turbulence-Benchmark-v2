from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -7
    result = []
    for i in range(len(circular_list)):
        subresult = []
        product = 1
        for j in range(i, len(circular_list) + i):
            num = circular_list[j % len(circular_list)]
            if product * num == n:
                subresult.append(num)
                product *= num
            elif product * num < 0:
                subresult = []
                product = 1
            else:
                break
        if subresult:
            result.append(subresult)
    return result