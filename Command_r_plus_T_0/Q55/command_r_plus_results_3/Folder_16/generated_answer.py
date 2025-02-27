def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        length = len(lst)
        product_sublists = []
        for i in range(length):
            product = 1
            sublist = []
            for j in range(i, length):
                product *= lst[j]
                sublist.append(lst[j])
                if product == target_product:
                    product_sublists.append(sublist)
                if product > target_product or product == 0:
                    break
        return product_sublists
    product_sublists = find_product_sublists(circular_list, -838)
    product_sublists.extend(find_product_sublists(circular_list[::-1], -838))
    return product_sublists