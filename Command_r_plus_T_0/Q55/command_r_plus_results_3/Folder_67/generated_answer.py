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
    result = []
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) + 1):
            sublist = circular_list[i:] + circular_list[:j]
            if len(sublist) <= len(circular_list):
                result += find_subarrays(sublist, 33, len(sublist))
    return result