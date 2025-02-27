def lists_with_product_equal_n(lst):
    n = -44
    result = []
    length = len(lst)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= lst[end % length]
            if product == n:
                sublist = lst[start:end + 1]
                if start > end:
                    sublist = lst[start:] + lst[:end + 1]
                result.append(sublist)
            elif product > abs(n) and n < 0 or (product < n and n >= 0):
                break
    return result