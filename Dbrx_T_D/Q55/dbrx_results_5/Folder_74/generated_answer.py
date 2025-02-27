from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    result = []
    n = 51
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sub_list = list(islice(cycle(circular_list[i:j + 1]), j - i + 1))
            if sub_list and sub_list[0] == 0 and (len(sub_list) > 1):
                sub_list = [0] + sub_list[1:]
            if sub_list and reduce(lambda x, y: x * y, sub_list, 1) == n:
                result.append(sub_list)
    return result