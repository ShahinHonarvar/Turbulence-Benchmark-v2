def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, size):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + size, len(arr))):
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
        subarray = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(subarray, 3, len(circular_list)))
    return result