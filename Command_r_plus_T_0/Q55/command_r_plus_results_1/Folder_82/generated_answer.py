def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, size):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, min(i + size, len(arr))):
                if prod(arr[i:j + 1]) == target:
                    subarrays.append(arr[i:j + 1])
        return subarrays

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    size = len(circular_list)
    result = []
    for i in range(size):
        for j in range(i, min(i + size, len(circular_list))):
            sublist = circular_list[i:j + 1]
            if prod(sublist) == 8:
                result.append(sublist)
    return result