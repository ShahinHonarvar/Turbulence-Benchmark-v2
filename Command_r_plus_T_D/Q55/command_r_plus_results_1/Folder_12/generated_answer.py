def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product, start, end):
        if start > end:
            return []
        if product == -18:
            return [arr[start:end + 1]]
        subarrays = []
        for i in range(start, end + 1):
            new_product = product * arr[i]
            if new_product == -18 or new_product / arr[i] == -18:
                subarrays.extend(find_subarrays(arr, new_product, start + 1, end))
        return subarrays
    sublists = []
    for i in range(len(circular_list)):
        sublists.extend(find_subarrays(circular_list, 1, i, i + len(circular_list) - 1))
    return sublists