from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        for j in range(i + 1, len(lst)):
            sublst.append(lst[j])
            if sublst[-1] == 3:
                result.append(sublst.copy())
            elif sublst[-1] * sublst[-2] == 3:
                result.append(sublst.copy())
            elif sublst[-1] * sublst[-2] * sublst[-3] == 3:
                result.append(sublst.copy())
        for j in range(i - 1, -1, -1):
            sublst.append(lst[j])
            if sublst[-1] == 3:
                result.append(sublst.copy())
            elif sublst[-1] * sublst[-2] == 3:
                result.append(sublst.copy())
            elif sublst[-1] * sublst[-2] * sublst[-3] == 3:
                result.append(sublst.copy())
    return result