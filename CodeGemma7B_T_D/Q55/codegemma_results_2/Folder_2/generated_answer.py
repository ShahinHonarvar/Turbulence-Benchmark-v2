from itertools import combinations_with_replacement as replace_comb

def lists_with_product_equal_n(c_list, n=-968):
    size = len(c_list)
    i = 0
    sublists = []
    while i < size:
        for r in range(1, size - i + 1):
            for comb in replace_comb(c_list, r):
                if all(comb):
                    product = comb[0]
                    pos = [i]
                    for j in range(1, r):
                        if pos and comb[j] * pos[-1] == product and (comb[j] not in c_list[pos[-1]:i + j]):
                            pos.append(pos[-1] + c_list[pos[-1]:i + j].index(comb[j]))
                        elif comb[j] * product == n and j == r - 1:
                            if comb[j] not in c_list[i:i + j]:
                                newi = i + c_list[i:i + j].index(comb[j])
                                pos.append(newi)
                            elif comb[j] in c_list[i:i + j] and r > j:
                                newi = i + c_list[i:i + j].index(comb[j])
                                pos.append(newi)
                            else:
                                break
                    factor = 1
                    for j in range(r):
                        factor *= comb[j]
                    if product == n and all(comb):
                        if factor > 0 and factor < n and (pos[-1] + 1 == i + r):
                            sublists.append(c_list[pos[0]:pos[0] + r])
                        elif factor < 0 and factor > n and (pos[-1] + 1 == i + r):
                            sublists.append(c_list[pos[0]:pos[0] + r])
                        elif factor > 0 and factor > n and (pos[0] + c_list[pos[0]:i + r].index(comb[r - 1]) + 1 == i + r):
                            sublists.append(c_list[pos[0]:pos[0] + r])
                        elif factor < 0 and factor < n and (pos[0] + c_list[pos[0]:i + r].index(comb[r - 1]) + 1 == i + r):
                            sublists.append(c_list[pos[0]:pos[0] + r])
                    i += r - 1
                else:
                    i += r - 1
                    break
    return sublists