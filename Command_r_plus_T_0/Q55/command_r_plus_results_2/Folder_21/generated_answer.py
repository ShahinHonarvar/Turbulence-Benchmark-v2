def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, n):
        result = []
        for i in range(len(arr)):
            product = 1
            subarray = []
            for j in range(i, min(i + n, len(arr))):
                product *= arr[j]
                subarray.append(arr[j])
                if product == target:
                    result.append(subarray)
        return result
    result = []
    for i in range(len(circular_list)):
        result += find_subarrays(circular_list, 851, len(circular_list))
        circular_list = circular_list[1:] + [circular_list[0]]
    return result