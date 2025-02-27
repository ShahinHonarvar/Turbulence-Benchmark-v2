def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left, right = ([0] * length, [length] * length)
        product = [1] * length
        for i in range(length):
            product[i] = arr[i] if target_product % arr[i] == 0 else target_product // arr[i]
        for i in range(length):
            if product[i] == 1:
                left[i] = 0
            else:
                left[i] = left[i - 1]
            right[i] = length
        for i in range(length - 1, -1, -1):
            if product[i] == target_product:
                left[i] = 0
                right[i] = min(right[i], right[i + 1])
        result = []
        for i in range(length):
            if product[i] == target_product:
                result.append(arr[left[i]:right[i]])
        return result
    sublists = find_subarrays(circular_list, -15)
    circular_sublists = []
    for sublist in sublists:
        circular_sublists.append(sublist + sublist[:1])
    return circular_sublists