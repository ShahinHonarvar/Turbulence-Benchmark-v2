def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, size):
        subarrays = []
        for i in range(len(arr)):
            product = 1
            for j in range(0, size):
                product *= arr[(i + j) % len(arr)]
                if product == target:
                    subarrays.append(arr[(i + j - size + 1) % len(arr):(i + 1) % len(arr)])
        return subarrays
    sublists = []
    for size in range(1, len(circular_list) + 1):
        sublists.extend(find_subarrays(circular_list, 632, size))
    return sublists