from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 851
    result = []
    circular_list = list(circular_list)
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = list(islice(cycle(circular_list[i:j + 1]), len(circular_list)))
            if j - i + 1 <= len(circular_list) and sublist and (sub_product(sublist) == n):
                result.append(sublist)
    return result

def sub_product(sublist):
    result = 1
    for num in sublist:
        result *= num
    return result