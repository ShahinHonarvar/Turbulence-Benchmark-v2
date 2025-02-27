def lists_with_product_equal_n(circular_list):

    def find_product_sublists(lst, target_product):
        length = len(lst)
        product_sublists = []
        for i in range(length):
            product = 1
            sublist = []
            for j in range(i, length):
                product *= lst[j]
                sublist.append(lst[j])
                if product == target_product:
                    product_sublists.append(sublist)
                if product > target_product:
                    break
        return product_sublists
    product_sublists = find_product_sublists(circular_list, 47)
    circular_list_reversed = circular_list[::-1]
    product_sublists_reversed = find_product_sublists(circular_list_reversed, 47)
    all_sublists = product_sublists + product_sublists_reversed
    unique_sublists = []
    for sublist in all_sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists