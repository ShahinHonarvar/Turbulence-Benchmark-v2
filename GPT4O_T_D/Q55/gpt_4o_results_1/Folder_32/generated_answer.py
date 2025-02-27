def lists_with_product_equal_n(circular_list):

    def find_sublist(start_index, n):
        sublists = []
        product = 1
        sublist = []
        for i in range(len(circular_list)):
            index = (start_index + i) % len(circular_list)
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product > n:
                break
            if product == n:
                sublists.append(list(sublist))
        return sublists
    result = []
    for i in range(len(circular_list)):
        result.extend(find_sublist(i, 76))
    return result