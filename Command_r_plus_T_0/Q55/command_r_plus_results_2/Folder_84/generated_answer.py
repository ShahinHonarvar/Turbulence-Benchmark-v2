def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        count = 0
        result = []
        for i in range(n):
            curr_product = 1
            for j in range(i, n):
                curr_product *= arr[j]
                if curr_product == target:
                    result.append(arr[i:j + 1])
                if curr_product > target:
                    break
        return result
    n = len(circular_list)
    target = -906
    result = []
    for i in range(n):
        subarray = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(subarray, target, n))
    return result