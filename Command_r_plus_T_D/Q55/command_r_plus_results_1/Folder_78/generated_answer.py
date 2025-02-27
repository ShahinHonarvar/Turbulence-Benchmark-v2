def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_74(lst: list[int], product: int=1) -> list[int]:
        if product == 74:
            return lst
        if product > 74:
            return []
        return [find_product_74(lst[i + 1:], product * lst[i]) for i in range(len(lst)) if product * lst[i] <= 74]
    result = []
    for i in range(len(circular_list)):
        sublists = find_product_74(circular_list[i:] + circular_list[:i])
        result.extend(sublists)
    return result