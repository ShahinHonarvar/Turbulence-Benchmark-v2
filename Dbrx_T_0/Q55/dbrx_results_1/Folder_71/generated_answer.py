from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 47
    result = []
    for i in range(len(circular_list)):
        sub_list = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if sub_list[0] == 0:
            continue
        if sub_list[0] * sub_list[1] == n:
            result.append(sub_list[:2])
        elif sub_list[0] * sub_list[1] * sub_list[2] == n:
            result.append(sub_list[:3])
        elif sub_list[0] * sub_list[1] * sub_list[2] * sub_list[3] == n:
            result.append(sub_list[:4])
        elif sub_list[0] * sub_list[1] * sub_list[2] * sub_list[3] * sub_list[4] == n:
            result.append(sub_list[:5])
    return result