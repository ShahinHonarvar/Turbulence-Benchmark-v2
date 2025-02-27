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
    products = []
    for i in range(len(circular_list)):
        for j in range(i, min(i + len(circular_list), len(circular_list))):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 83:
                products.append(sublist)
    return products