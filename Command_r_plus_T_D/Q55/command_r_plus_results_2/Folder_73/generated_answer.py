def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_contiguous_sublists(lst: list[int]) -> list[list[int]]:
        length = len(lst)
        return [lst[i:j] for i in range(length) for j in range(i + 1, length + 1)]

    def product_equal_to_40(lst: list[int]) -> bool:
        return all(lst) and all((isinstance(i, int) for i in lst)) and (eval('*'.join(map(str, lst))) == 40)
    contiguous_sublists = get_contiguous_sublists(circular_list)
    return [sublist for sublist in contiguous_sublists if product_equal_to_40(sublist)]