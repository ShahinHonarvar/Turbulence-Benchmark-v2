def power(n):
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j + 1):
                product *= k
            if product == n:
                result = max(result, j - i + 1)
    return result

def lists_with_product_equal_n(lst):
    size = len(lst)
    if size < 2:
        return []
    if size == 2:
        return [lst] if lst[0] * lst[1] == 47 else []
    max_size = power(size)
    result = []
    for i in range(size):
        product = 1
        for j in range(i, size + max_size):
            product *= lst[j % size]
            if product == 47:
                result.append(lst[i:j % size + max_size])
                i = j % size
                break
    return result