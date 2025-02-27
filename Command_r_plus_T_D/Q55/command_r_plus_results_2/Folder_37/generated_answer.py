def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + n, len(arr))):
                if product(arr[i:j + 1]) == target:
                    result.append(arr[i:j + 1])
        return result

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    sublists = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], -76, len(circular_list))
        sublists.extend(subarrays)
    return sublists