def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, size):
        result = []
        for i in range(len(arr)):
            product = 1
            subarray = []
            for j in range(i, min(i + size, len(arr))):
                product *= arr[j]
                subarray.append(arr[j])
                if product == target:
                    result.append(subarray)
        return result
    sublists = find_subarrays(circular_list, 3, len(circular_list))
    return sublists