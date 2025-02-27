def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(lst: list[int], n: int) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == n
    n = -72
    list_length = len(circular_list)
    all_sublists = []
    for i in range(list_length):
        for j in range(i, list_length + i):
            sublist = circular_list[i:j] % list_length
            if product_equal_n(sublist, n):
                all_sublists.append(sublist)
    return all_sublists