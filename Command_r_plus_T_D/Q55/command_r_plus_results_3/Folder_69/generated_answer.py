def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for i in range(length):
            for j in range(i, length):
                if product(arr[i:j + 1]) == 90:
                    result.append(arr[i:j + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    subarrays = find_subarrays(circular_list, product)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray)
        for i in range(1, len(subarray)):
            circular_subarrays.append(subarray[-i:] + subarray[:-i])
    return circular_subarrays