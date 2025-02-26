def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(n):
            current_sublist = []
            current_product = 1
            k = 0
            while k < n:
                current_index = (i + k) % n
                current_sublist.append(lst[current_index])
                current_product *= lst[current_index]
                if current_product == 29:
                    result.append(current_sublist.copy())
                    break
                if current_product > 29:
                    break
                k += 1
    return result