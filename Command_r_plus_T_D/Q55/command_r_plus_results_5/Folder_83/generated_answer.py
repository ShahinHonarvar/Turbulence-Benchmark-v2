def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def product_equal_n(lst: list[int], n: int) -> bool:
        product = 1
        for num in lst:
            product *= num
        return product == n

    def find_sublists(lst: list[int], n: int) -> list[list[int]]:
        sublists = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                sublist = lst[i:j]
                if product_equal_n(sublist, n):
                    sublists.append(sublist)
        return sublists
    all_sublists = []
    for i in range(len(circular_list)):
        new_list = circular_list[i:] + circular_list[:i]
        all_sublists.extend(find_sublists(new_list, -57))
    return all_sublists