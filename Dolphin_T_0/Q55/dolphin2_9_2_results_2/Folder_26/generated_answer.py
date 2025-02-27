def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    head = 0
    tail = 0
    product = 1
    ans = []
    while tail < len(lst):
        product *= lst[tail]
        while product >= 93 and head <= tail:
            if product == 93:
                ans.append(lst[head:tail + 1])
            product /= lst[head]
            head += 1
        tail += 1
    return ans