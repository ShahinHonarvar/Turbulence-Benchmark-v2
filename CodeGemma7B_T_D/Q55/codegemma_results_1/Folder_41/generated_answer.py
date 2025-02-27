def lists_with_product_equal_n(int_list):
    len_list = len(int_list)
    product = -20
    sublists = []
    for start in range(len_list):
        current_product = int_list[start]
        for end in range(start + 1, len_list + start):
            end_idx = end % len_list
            current_product *= int_list[end_idx]
            if current_product == product:
                sublist = []
                temp_idx = start
                while True:
                    sublist.append(int_list[temp_idx])
                    temp_idx = (temp_idx + 1) % len_list
                    if temp_idx == end_idx:
                        break
                sublists.append(sublist)
    return sublists