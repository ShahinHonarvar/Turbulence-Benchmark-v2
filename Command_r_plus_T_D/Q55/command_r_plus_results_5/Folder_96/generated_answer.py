def lists_with_product_equal_n(circular_list):

    def find_zero_product_sublists(lst):
        result = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if prod(lst[i:j + 1]) == 0:
                    result.append(lst[i:j + 1])
        return result

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    all_sublists = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        all_sublists.extend(find_zero_product_sublists(sublist))
    unique_sublists = []
    for sublist in all_sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists