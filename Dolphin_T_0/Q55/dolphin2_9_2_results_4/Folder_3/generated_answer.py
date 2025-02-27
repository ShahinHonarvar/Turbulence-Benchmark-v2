def lists_with_product_equal_n(a):
    n = -22
    result = []
    product = 1
    left_idx = 0
    right_idx = 0
    for i in range(len(a)):
        product *= a[i]
        right_idx += 1
        while product > n:
            product /= a[left_idx]
            left_idx += 1
        if product == n:
            if left_idx == 0:
                right_idx -= 1
            while left_idx <= right_idx:
                result.append(a[left_idx:right_idx + 1])
                left_idx += 1
    return result