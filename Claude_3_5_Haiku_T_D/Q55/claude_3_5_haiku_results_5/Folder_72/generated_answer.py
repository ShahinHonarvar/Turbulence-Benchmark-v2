def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            current_sublist = [lst[i % n] for i in range(start, end + 1)]
            product = 1
            for num in current_sublist:
                product *= num
            if product == 10:
                result.append(current_sublist)
    return result