def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        length = len(lst)
        for i in range(length):
            for j in range(i, length):
                if i == j:
                    if lst[i] == product:
                        yield [lst[i]]
                else:
                    subarray_product = lst[i]
                    for k in range(i + 1, j + 1):
                        subarray_product *= lst[k]
                    if subarray_product == product:
                        yield lst[i:j + 1]
    return list(find_subarrays(circular_list, -89))