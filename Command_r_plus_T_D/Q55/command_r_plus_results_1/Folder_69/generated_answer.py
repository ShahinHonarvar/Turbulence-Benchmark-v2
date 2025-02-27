def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= arr[j]
                if product == target:
                    result.append(arr[i:j + 1])
                if product > target:
                    break
        return result
    result = []
    for i in range(len(circular_list)):
        temp_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(temp_list, 90, len(temp_list)))
    return result