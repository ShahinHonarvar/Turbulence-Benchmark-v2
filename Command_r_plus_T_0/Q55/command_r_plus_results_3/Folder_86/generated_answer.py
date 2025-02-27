def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for i in range(length):
            product_so_far = 1
            for j in range(i, length):
                product_so_far *= arr[j % length]
                if product_so_far == product:
                    result.append(arr[i:j + 1])
                if product_so_far * arr[(j + 1) % length] == product:
                    result.append(arr[i:j + 2])
        return result
    subarrays = find_subarrays(circular_list, -779)
    unique_subarrays = [tuple(sub) for sub in subarrays]
    unique_set = set(unique_subarrays)
    unique_list = list(unique_set)
    final_result = [list(sub) for sub in unique_list]
    return final_result