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
                if product > target_product or j == length - 1:
                    break
        return product_sublists
    product_sublists = find_product_sublists(circular_list, -6)
    circular_list_reversed = circular_list[::-1]
    product_sublists_reversed = find_product_sublists(circular_list_reversed, -6)
    unique_sublists = product_sublists + product_sublists_reversed
    unique_sublists = list(set(map(tuple, unique_sublists)))
    result = [list(sublist) for sublist in unique_sublists]
    return result