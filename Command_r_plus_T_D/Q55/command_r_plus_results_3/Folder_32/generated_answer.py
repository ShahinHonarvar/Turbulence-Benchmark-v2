def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_76_sublists(lst: list[int], product: int=1, sublist: list[int]=[]) -> list[list[int]]:
        if product == 76:
            return [sublist]
        sublists = []
        for i in range(len(lst)):
            product *= lst[i]
            sublist.append(lst[i])
            sublists.extend(find_product_76_sublists(lst[i + 1:], product, sublist.copy()))
            product //= lst[i]
            sublist.pop()
        return sublists
    return find_product_76_sublists(circular_list)