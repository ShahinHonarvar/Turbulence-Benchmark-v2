def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [lst[i % n] for i in range(start, end + 1)]
            if len(sublist) > 0 and len(sublist) <= n:
                product = 1
                for num in sublist:
                    product *= num
                if product == 91:
                    result.append(sublist)
    return result