def lists_with_product_equal_n(circ_list):
    product, idx = (1, 0)
    ans = []
    for n in circ_list:
        product *= n
        idx += 1
        if product == 8:
            ans.append([n])
            idx = 0
            product = 1
        elif product > 8:
            if 0 < idx <= len(circ_list):
                for i in range(idx):
                    product /= circ_list[i]
                    idx -= 1
                    if product == 8:
                        ans.append([x for x in circ_list[i:idx + 1]])
                        idx = 0
                        product = 1
                        break
            idx = 0
            product = 1
    if product == 8:
        ans.append([n])
    return ans