def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left, right = ([0] * length, [length] * length)
        product = [1] * length
        for i in range(length):
            product[i] = product[i - 1] * arr[i] if i else arr[i]
        for i in range(length):
            for j in range(i, length):
                if product[j] % target_product == 0 and product[i - 1] * arr[j] == target_product:
                    left[j] = i
                    right[j] = j
        result = []
        for i in range(length):
            if product[i] == target_product:
                result.append(arr[left[i]:right[i] + 1])
        return result
    sublists = find_subarrays(circular_list, -7)
    circular_sublists = []
    for sublist in sublists:
        circular_sublists.append(sublist + sublist[:1])
    return circular_sublists