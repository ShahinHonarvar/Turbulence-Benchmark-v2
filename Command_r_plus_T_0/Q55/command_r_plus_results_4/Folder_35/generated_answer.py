def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, size):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + size, len(arr))):
                if product(arr[i:j + 1]) == target:
                    result.append(arr[i:j + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    sublists = find_subarrays(circular_list, 83, len(circular_list))
    return sublists