def lists_with_product_equal_n(circular_list):
    for k in range(len(circular_list)):
        circular_list.append(circular_list[0])
        for i in range(k):
            for j in range(i + 2, len(circular_list)):
                if circular_list[i] * circular_list[i + 1] * circular_list[j] * circular_list[j + 1] == 45:
                    if [circular_list[i], circular_list[i + 1], circular_list[j], circular_list[j + 1]] not in sublists:
                        sublists.append([circular_list[i], circular_list[i + 1], circular_list[j], circular_list[j + 1]])
        circular_list.pop(0)
    return sublists