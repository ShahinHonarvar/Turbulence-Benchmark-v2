def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product, start, end):
        if start > end:
            return []
        if product == 1:
            return [lst[start:end + 1]]
        result = []
        for i in range(start, end + 1):
            new_product = product * lst[i]
            if new_product == -46 or new_product == 46:
                result.extend(find_subarrays(lst, new_product, start, i - 1))
                result.extend(find_subarrays(lst, 1, i + 1, end))
                break
        return result
    sublists = []
    for i in range(len(circular_list)):
        sublists.extend(find_subarrays(circular_list, 1, i, i + len(circular_list) - 1))
    return [sublist for sublist in sublists if abs(prod(sublist)) == 46]