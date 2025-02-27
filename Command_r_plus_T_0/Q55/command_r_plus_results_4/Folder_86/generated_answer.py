def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            product = 1
            for j in range(i, n + i):
                product *= arr[j % n]
                if product == target:
                    result.append(arr[i:j + 1])
                if product > target:
                    break
        return result
    if not circular_list:
        return []
    product_list = find_subarrays(circular_list, -779, len(circular_list))
    return product_list