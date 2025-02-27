def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        result = []
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(i, len(lst)):
                product *= lst[j]
                sublist.append(lst[j])
                if product == target_product:
                    result.append(sublist)
                if product > target_product:
                    break
        return result
    all_sublists = find_product_sublists(circular_list, -51)
    all_sublists.extend(find_product_sublists(circular_list[::-1], -51))
    unique_sublists = []
    for sublist in all_sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists