def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_equal_subsets(target_product: int, subset: list[int]) -> list[list[int]]:
        if target_product == 1:
            return [subset[:]]
        sublists = []
        for i in range(len(subset)):
            for j in range(i + 1, len(subset) + 1):
                sub = subset[i:j]
                product = 1
                for num in sub:
                    product *= num
                if product == target_product:
                    sublists.append(sub[:])
        return sublists
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) > len(circular_list):
                break
            product_sublists = find_product_equal_subsets(-17, sublist)
            result.extend(product_sublists)
    return result