def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if product == 1:
                    subarrays.append(lst[i:j])
                else:
                    temp_product = 1
                    for k in range(i, j + 1):
                        temp_product *= lst[k]
                    if temp_product == product:
                        subarrays.append(lst[i:j + 1])
        return subarrays
    sublists = find_subarrays(circular_list, 6)
    sublists.extend(find_subarrays(circular_list[::-1], 6))
    return sublists