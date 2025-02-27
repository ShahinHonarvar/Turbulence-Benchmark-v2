def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    if n == 0:
        return result
    if n == 1:
        if lst[0] == -690:
            result.append([lst[0]])
        return result
    for i in range(n):
        product = 1
        left = i
        right = i
        while right != i - 1:
            product *= lst[right]
            if product > 690:
                break
            if product == 690 and left != right:
                result.append(lst[left:right + 1])
                break
            right = (right + 1) % n
            if right == 0:
                left = (left - 1) % n
                if left < 0:
                    left += n
    return result