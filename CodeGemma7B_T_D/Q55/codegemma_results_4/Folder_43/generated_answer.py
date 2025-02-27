def lists_with_product_equal_n(circular_list):
    subs = []
    for sublist_size in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            if sum(circular_list[i:i + sublist_size]) == -26 and len(circular_list[i:i + sublist_size]) == sublist_size:
                subs.append(circular_list[i:i + sublist_size])
    return subs