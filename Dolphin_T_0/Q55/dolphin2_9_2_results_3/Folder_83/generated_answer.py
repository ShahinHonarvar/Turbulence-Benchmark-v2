def lists_with_product_equal_n(lst, n=-57):
    result = []
    for i in range(len(lst)):
        temp_lst = [lst[i]]
        product = lst[i]
        for j in ((i + 1) % len(lst), (i + 2) % len(lst), (i + 3) % len(lst))[:len(lst) - i]:
            temp_lst.append(lst[(i + j) % len(lst)])
            product *= lst[(i + j) % len(lst)]
            if product % n == 0 and sorted(temp_lst) not in result:
                result.append(sorted(temp_lst))
    return result