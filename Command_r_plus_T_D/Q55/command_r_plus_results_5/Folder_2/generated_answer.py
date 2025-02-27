def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count = 0
        subarrays = []
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= arr[j]
                if product == target:
                    subarrays.append(arr[i:j + 1])
                if product > target:
                    break
        return subarrays
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(sublist, -968, len(circular_list)))
    return result