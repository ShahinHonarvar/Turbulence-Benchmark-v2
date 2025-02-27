def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product, start, end):
        if start > end:
            return []
        if product == -23:
            return [lst[start:end + 1]]
        subarrays = []
        for i in range(start, end + 1):
            new_product = product * lst[i]
            if new_product == -23:
                subarrays.append(lst[start:i + 1])
            elif new_product < -23 and i < end:
                subarrays.extend(find_subarrays(lst, new_product, i + 1, end))
        return subarrays
    sublists = []
    for i in range(len(circular_list)):
        sublists.extend(find_subarrays(circular_list, 1, i, i + len(circular_list) - 1))
    return sublists