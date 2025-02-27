def product_equal_n(lst, n):
    result = []
    if not lst:
        return result
    length = len(lst)
    prefix = [1]
    for x in lst:
        prefix.append(prefix[-1] * x)
    for i in range(length):
        for j in range(i + 1, length + 1):
            if prefix[j] / prefix[i] == n:
                result.append(lst[i:j])
    return result