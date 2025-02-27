def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_36_sublists(lst: list[int], start: int, end: int) -> list[list[int]]:
        product = 1
        for i in range(start, end + 1):
            product *= lst[i]
            if product == 36:
                yield lst[start:end + 1]
            if product > 36:
                break
    sublists = []
    for i in range(len(circular_list)):
        for sublist in find_product_36_sublists(circular_list, i, i + 3):
            sublists.append(sublist)
    return sublists