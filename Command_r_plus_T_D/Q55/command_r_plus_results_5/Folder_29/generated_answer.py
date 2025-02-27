def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        subarrays = []
        for i in range(len(arr)):
            product = 1
            for j in range(i, len(arr)):
                product *= arr[j]
                if product == target_product:
                    subarrays.append(arr[i:j + 1])
                if product > target_product:
                    break
        return subarrays
    sublists = find_subarrays(circular_list, 15)
    sublists.extend(find_subarrays(circular_list[1:], 15))
    return sublists