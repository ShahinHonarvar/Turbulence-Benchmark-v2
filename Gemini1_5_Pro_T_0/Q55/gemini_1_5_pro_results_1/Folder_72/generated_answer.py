def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, i + n):
            sublist = circular_list[i:j % n] + circular_list[:j % n] if j >= n else circular_list[i:j]
            if len(sublist) <= n:
                product = 1
                for x in sublist:
                    product *= x
                if product == 10:
                    sublists.append(sublist)
    return sublists