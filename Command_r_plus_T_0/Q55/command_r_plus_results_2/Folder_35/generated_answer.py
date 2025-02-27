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
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if len(sublist) <= len(circular_list):
                product = 1
                for num in sublist:
                    product *= num
                if product == 83:
                    result.append(sublist)
    return result