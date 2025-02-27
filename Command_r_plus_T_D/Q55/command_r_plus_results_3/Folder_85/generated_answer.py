def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(lst: list[int]) -> list[list[int]]:
        sublists = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                sublists.append(lst[i:j + 1])
        return sublists

    def product_equals_n(sublist: list[int], n: int) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == n
    result = []
    for sublist in get_contiguous_sublists(circular_list):
        if product_equals_n(sublist, -97):
            result.append(sublist)
    return result