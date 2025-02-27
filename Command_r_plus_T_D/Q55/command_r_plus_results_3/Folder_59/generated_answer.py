def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for i in range(length):
            product_so_far = 1
            for j in range(i, length):
                product_so_far *= arr[j]
                if product_so_far == product:
                    result.append(arr[i:j + 1])
                if product_so_far > product:
                    break
        return result
    subarrays = find_subarrays(circular_list, -3)
    circular_subarrays = []
    for subarray in subarrays:
        circular_subarrays.append(subarray + subarray[:1])
    result = []
    for subarray in circular_subarrays:
        product_so_far = 1
        for num in subarray:
            product_so_far *= num
            if product_so_far == -3:
                result.append(list(subarray[:len(subarray) - (product_so_far != -3)]))
                break
    return result