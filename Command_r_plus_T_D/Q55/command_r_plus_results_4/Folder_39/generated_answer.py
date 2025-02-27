def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            curr_product = 1
            for j in range(i, n + i):
                curr_product *= arr[j % n]
                if curr_product == target:
                    result.append(arr[i:j + 1])
                if curr_product > target:
                    break
        return result
    sublists = []
    product = -46
    for i in range(len(circular_list)):
        subarray_product = 1
        subarray = []
        for j in range(i, len(circular_list) + i):
            subarray.append(circular_list[j % len(circular_list)])
            subarray_product *= subarray[-1]
            if subarray_product == product:
                sublists.append(subarray)
                subarray_product = 1
                subarray = []
            if subarray_product > product:
                break
    sublists.extend(find_subarrays(circular_list, product, len(circular_list)))
    return sublists