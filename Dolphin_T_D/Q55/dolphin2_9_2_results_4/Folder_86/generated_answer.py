def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    lst.extend(lst)
    for head in range(0, size):
        product = 1
        for tail in range(head, head + size):
            product *= lst[tail]
            if product == -779 and lst[tail] != 1 and (lst[head] != 1):
                sublist = lst[head:tail + 1]
                result.append(list(sublist))
            if product > -779:
                break
    return result