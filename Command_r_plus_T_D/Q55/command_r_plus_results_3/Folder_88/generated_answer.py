def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(lst: list[int], n: int) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == n

    def find_sublists(lst: list[int], n: int) -> list[list[int]]:
        length = len(lst)
        sublists = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                sublist = lst[start:start + size]
                if product_equal_n(sublist, n):
                    sublists.append(sublist)
        return sublists
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_sublists(temp_list, -56))
    return result