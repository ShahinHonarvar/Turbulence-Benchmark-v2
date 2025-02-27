def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_zero_product_sublists(lst: list[int]) -> list[list[int]]:
        result = []
        product = 1
        for num in lst:
            if num == 0:
                result.append([0])
                product = 1
            elif product == 0:
                product = 0
            else:
                product *= num
        if product == 0:
            result.append(lst)
        return result
    zero_product_sublists = find_zero_product_sublists(circular_list)
    zero_product_sublists.extend(find_zero_product_sublists(circular_list[1:]))
    unique_sublists = []
    for sublist in zero_product_sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists