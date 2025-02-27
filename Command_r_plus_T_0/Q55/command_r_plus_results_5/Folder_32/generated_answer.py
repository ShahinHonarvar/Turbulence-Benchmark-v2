def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1 and size > 1:
                    break
                if product == arr[start:start + size].prod():
                    result.append(arr[start:start + size])
        return result
    sublists = find_subarrays(circular_list, 76)
    sublists.extend(find_subarrays(circular_list[1:] + [circular_list[0]], 76))
    return sublists