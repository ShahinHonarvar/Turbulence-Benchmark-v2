def lists_with_product_equal_n(circular_list):
    factors = {-3, 3, -9, 9, -27, 27, -81, 81}
    result = []
    curr = 0
    prod = 1
    curr_list = []
    while curr < len(circular_list):
        if circular_list[curr] not in factors:
            curr += 1
            continue
        if circular_list[curr] in factors:
            prod *= circular_list[curr]
            curr += 1
            curr_list.append(circular_list[curr - 1])
        while circular_list[curr] in factors and prod == -81:
            result.append(curr_list)
            prod /= circular_list[curr]
            curr -= 1
            curr_list.pop()
    return result