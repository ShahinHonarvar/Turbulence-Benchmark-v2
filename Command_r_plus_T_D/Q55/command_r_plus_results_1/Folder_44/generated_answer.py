def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target_product, size):
        result = []
        for i in range(len(arr)):
            product = 1
            subarray = []
            for j in range(i, min(i + size, len(arr))):
                product *= arr[j]
                subarray.append(arr[j])
                if product == target_product:
                    result.append(subarray)
        return result
    result = []
    for i in range(len(circular_list)):
        for sublist in find_subarrays(circular_list[i:] + circular_list[:i], 29, len(circular_list)):
            result.append(sublist)
    return result