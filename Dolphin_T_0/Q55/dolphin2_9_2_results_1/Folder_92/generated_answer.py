def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        start = i
        end = i
        while start >= 0 and end < n:
            if product == 5:
                temp = lst[start:end + 1]
                if temp not in result:
                    result.append(temp)
            product *= lst[end]
            if product < 5:
                end += 1
            else:
                start -= 1
    return result