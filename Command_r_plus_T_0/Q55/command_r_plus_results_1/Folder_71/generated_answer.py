def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + n, len(arr))):
                if prod(arr[i:j + 1]) == target:
                    result.append(arr[i:j + 1])
        return result

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for i in range(n):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], 47, n)
        result.extend(subarrays)
    return result