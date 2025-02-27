from itertools import islice, cycle

def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        sublst = [lst[i]]
        for j in range(i + 1, len(lst)):
            sublst.append(lst[j])
            if sublst[-1] == 0:
                break
            if sublst[-1] == 1:
                continue
            if sublst[-1] == 2:
                if 3 in sublst:
                    break
                else:
                    result.append(sublst.copy())
                    break
            if sublst[-1] == 3:
                if 2 in sublst:
                    result.append(sublst.copy())
                    break
                else:
                    continue
            if sublst[-1] == 6:
                result.append(sublst.copy())
                break
            if sublst[-1] % 2 == 0:
                if sublst[-1] // 2 in sublst:
                    result.append(sublst.copy())
                    break
                else:
                    continue
            if sublst[-1] % 3 == 0:
                if sublst[-1] // 3 in sublst:
                    result.append(sublst.copy())
                    break
                else:
                    continue
        for k in range(i - 1, -1, -1):
            sublst.insert(0, lst[k])
            if sublst[0] == 0:
                break
            if sublst[0] == 1:
                continue
            if sublst[0] == 2:
                if 3 in sublst:
                    break
                else:
                    result.append(sublst.copy())
                    break
            if sublst[0] == 3:
                if 2 in sublst:
                    result.append(sublst.copy())
                    break
                else:
                    continue
            if sublst[0] == 6:
                result.append(sublst.copy())
                break
            if sublst[0] % 2 == 0:
                if sublst[0] // 2 in sublst:
                    result.append(sublst.copy())
                    break
                else:
                    continue
            if sublst[0] % 3 == 0:
                if sublst[0] // 3 in sublst:
                    result.append(sublst.copy())
                    break
                else:
                    continue
    return result