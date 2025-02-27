import itertools

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(1 << n):
        bit_mask = bin(i)[2:].zfill(n)
        product = 1
        sublist = []
        for j in range(n):
            if bit_mask[j]:
                sublist.append(lst[j])
                if j > 0:
                    product *= sublist[-1] - sublist[0]
                else:
                    product *= sublist[-1]
            elif sublist:
                break
            if product:
                result.append(sublist)
    return result