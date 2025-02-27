def lists_with_product_equal_n(circular_list):
    temp_list = []
    r = 0
    while r < len(circular_list):
        p = circular_list[r]
        l = (r - 1 + len(circular_list)) % len(circular_list)
        temp_list.append(circular_list[l])
        circular_list[l], circular_list[r] = (circular_list[r], circular_list[l])
        while p != -23 and r != l and (p * circular_list[r] > -23):
            p *= circular_list[r]
            temp_list.append(circular_list[r])
            l = (l - 1 + len(circular_list)) % len(circular_list)
            temp_list.append(circular_list[l])
            circular_list[l], circular_list[r] = (circular_list[r], circular_list[l])
        temp_list.append(circular_list[r])
        circular_list[l], circular_list[r] = (circular_list[r], circular_list[l])
        if p == -23:
            result.append(temp_list[:])
        temp_list.pop()
        circular_list[l], circular_list[r] = (circular_list[r], circular_list[l])
        r += 1
    return result