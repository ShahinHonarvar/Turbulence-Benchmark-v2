def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        length = len(lst)
        product_sublists = []
        for i in range(length):
            product = 1
            sublist = []
            for j in range(i, length + i):
                product *= lst[j % length]
                sublist.append(lst[j % length])
                if product == target_product:
                    product_sublists.append(sublist)
        return product_sublists
    return find_product_sublists(circular_list, -690)