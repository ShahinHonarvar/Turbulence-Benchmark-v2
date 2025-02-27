def lists_with_product_equal_n(circ_lst):
    if not circ_lst or len(circ_lst) == 1:
        return []
    for i in range(len(circ_lst)):
        product = circ_lst[i]
        j = i + 1
        while product != 10 and j < len(circ_lst):
            product *= circ_lst[j]
            j += 1
            if product == 10:
                return [[circ_lst[k] for k in range(i, j)]]
        if product == 10:
            dup = set()
            for k in range(i, j):
                dup.add(tuple(circ_lst[k:j + 1]))
            for sub in dup:
                if sub not in output:
                    output.append(list(sub))
    return output