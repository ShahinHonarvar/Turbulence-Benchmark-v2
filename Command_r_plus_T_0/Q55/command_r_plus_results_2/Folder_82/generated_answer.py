def lists_with_product_equal_n(circular_list):

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
    result = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], 8, len(circular_list))
        result.extend(subarrays)
    return result