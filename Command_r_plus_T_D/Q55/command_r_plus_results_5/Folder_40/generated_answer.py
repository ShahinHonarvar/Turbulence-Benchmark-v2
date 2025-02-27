def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        sublists = []
        product = 1
        start = 0
        for end in range(len(lst)):
            product *= lst[end]
            if product == target_product:
                sublists.append(lst[start:end + 1])
            if product == target_product and lst[end] == lst[start] * target_product:
                start += 1
                product = 1
        return sublists
    all_sublists = []
    for i in range(len(circular_list)):
        rotated_list = circular_list[i:] + circular_list[:i]
        sublists = find_product_sublists(rotated_list, -9)
        all_sublists.extend(sublists)
    return all_sublists