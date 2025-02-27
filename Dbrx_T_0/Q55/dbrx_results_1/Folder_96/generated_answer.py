from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = 0
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if sublist[0] == 0:
            result.append(sublist)
        elif n == 0:
            n = sublist[0]
        elif n != 0 and sublist[0] != 0:
            for j in range(1, len(sublist)):
                if sublist[j] * n == 0:
                    result.append(sublist[:j + 1])
                    break
                n *= sublist[j]
                if n == 0:
                    break
    return result