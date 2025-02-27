def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            product = 1
            for j in range(n):
                product *= arr[(i + j) % n]
                if product == target:
                    result.append(arr[(i + j + 1) % n:(i + j + 1) % n + n])
        return result
    result = []
    for i in range(len(circular_list)):
        subarray = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(subarray, -83, len(circular_list)))
    return result