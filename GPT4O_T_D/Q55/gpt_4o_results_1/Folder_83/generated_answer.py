def lists_with_product_equal_n(circular_list):

    def subarray_product_equals_k(arr, n, k):
        subarrays = []
        for i in range(n):
            prod = 1
            for j in range(i, i + n):
                prod *= arr[j % n]
                if prod == k:
                    subarrays.append([arr[x % n] for x in range(i, j + 1)])
        return subarrays
    return subarray_product_equals_k(circular_list, len(circular_list), -57)