def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= arr[j]
                if product == target:
                    result.append(arr[i:j + 1])
                if product > target:
                    break
        return result
    target_product = 733
    unique_elements = set(circular_list)
    max_len = len(unique_elements)
    all_permutations = []
    for length in range(1, max_len + 1):
        permutations = []
        for sublist in circular_list:
            if len(sublist) == length:
                permutations.append(sublist)
        all_permutations.extend(permutations)
    valid_sublists = find_subarrays(all_permutations, target_product, len(all_permutations))
    return valid_sublists