def lists_with_product_equal_n(lst):
    for i in range(len(lst)):
        start = i
        product = 1
        sublist = []
        while True:
            sublist.append(lst[start])
            product *= lst[start]
            start = (start + 1) % len(lst)
            if product == 90:
                break
            elif product > 90:
                product //= lst[i]
                i += 1
                break
            elif len(sublist) > len(lst):
                break
    return sublist