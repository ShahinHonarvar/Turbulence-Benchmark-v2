def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_subsets(product, start, current_product, current_subset):
        if current_product == product:
            result.append(current_subset[:])
        for i in range(start, len(circular_list)):
            current_subset.append(circular_list[i])
            current_product *= circular_list[i]
            find_product_subsets(product, i + 1, current_product, current_subset)
            current_product /= circular_list[i]
            current_subset.pop()
    result = []
    for i in range(len(circular_list)):
        find_product_subsets(-54, i, 1, [circular_list[i]])
    return result