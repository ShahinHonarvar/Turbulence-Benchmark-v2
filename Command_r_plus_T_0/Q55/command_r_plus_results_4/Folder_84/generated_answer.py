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
    target_product = -906
    unique_elements = set(circular_list)
    unique_products = [target_product // i for i in unique_elements if target_product % i == 0]
    all_subarrays = []
    for product in unique_products:
        subarrays = find_subarrays(circular_list, product, len(circular_list))
        all_subarrays.extend(subarrays)
    valid_subarrays = [subarray for subarray in all_subarrays if product(subarray) == target_product]
    return valid_subarrays