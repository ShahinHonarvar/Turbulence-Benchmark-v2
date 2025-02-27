def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(lst: list[int], target_product: int) -> list[list[int]]:
        product_sublists = []
        product = 1
        for i in range(len(lst)):
            product *= lst[i]
            if product == target_product:
                product_sublists.append(lst[i - len(lst) + 1:i + 1])
            if product > target_product:
                break
        return product_sublists
    product_sublists = find_product_sublists(circular_list, 415)
    product_sublists.extend(find_product_sublists(circular_list[::-1], 415))
    return product_sublists