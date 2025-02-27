def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            window = lst[j % n:]
            if 0 in window:
                break
            product = 1
            for num in window:
                product *= num
                if product > 33:
                    break
                if product == 33:
                    result.append(window[:window.index(num) + 1])
    return result