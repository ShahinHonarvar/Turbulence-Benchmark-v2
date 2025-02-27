def lists_with_product_equal_n(lst):
    n = len(lst)
    head = 0
    tail = n - 1
    current = 0
    sublists = []
    while current < n:
        if lst[head] * lst[current] == -20:
            sublist = [lst[head], lst[current]]
            if sublist not in sublists and len(sublist) <= n:
                sublists.append([sublist])
        else:
            head = (head + 1) % n
            tail = (tail + 1) % n
            current = (current + 1) % n
    return sublists