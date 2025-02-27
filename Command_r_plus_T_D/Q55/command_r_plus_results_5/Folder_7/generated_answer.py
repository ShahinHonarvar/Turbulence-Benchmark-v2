def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if product == 1:
                    subarrays.append(lst[i:j])
                    break
                if product == lst[j] and j - i + 1 <= len(lst):
                    subarrays.append(lst[i:j + 1])
                    product //= lst[j]
        return subarrays
    subarrays = find_subarrays(circular_list, 537)
    subarrays.extend(find_subarrays(circular_list[::-1], 537))
    return subarrays