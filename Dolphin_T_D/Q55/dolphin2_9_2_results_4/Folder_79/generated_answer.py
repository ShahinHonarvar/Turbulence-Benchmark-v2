def lists_with_product_equal_n(lst):
    n = len(lst)
    my_list = []
    for i in range(n):
        product = 1
        counter_list = []
        for j in range(i, n):
            product *= lst[j % n]
            counter_list.append(lst[j % n])
            if product == -83:
                my_list.append(counter_list)
    return my_list