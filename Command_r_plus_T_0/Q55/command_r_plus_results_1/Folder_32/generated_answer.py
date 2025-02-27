def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if arr[start:end + 1] not in result and product(arr[start:end + 1]) == product:
                    result.append(arr[start:end + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    return find_subarrays(circular_list, 76)