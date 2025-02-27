def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product(arr[start:start + size]):
                    result.append(arr[start:start + size])
        return result

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p == -61
    return find_subarrays(circular_list, product)