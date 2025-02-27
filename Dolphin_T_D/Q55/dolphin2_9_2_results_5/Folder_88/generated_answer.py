def lists_with_product_equal_n(lst, n=-56):
    result = []
    length = len(lst)
    left, right = (0, 1)
    mult = 1
    while right < length:
        if mult < n:
            mult *= lst[right]
            right += 1
            if right + 1 == length:
                right = 0
        while mult > n and left <= right:
            if right + 1 == length:
                right = 0
            mult /= lst[left]
            if left + 1 == length:
                left = 0
            else:
                left += 1
        while mult == n and right <= left + length:
            if right + 1 == length:
                right = 0
            else:
                right += 1
            result.append(lst[left:right + 1])
            if right + 1 == length:
                right = 0
            else:
                right += 1
            mult = 1
            left = 0
    return result