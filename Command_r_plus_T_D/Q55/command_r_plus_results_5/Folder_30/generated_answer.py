def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        left, right = ([0] * length, [length] * length)
        product_so_far = [1] * length
        for i in range(length):
            product_so_far[i] = product_so_far[i - 1] * arr[i] if i else arr[i]
            if product_so_far[i] == 1:
                left[i] = 0
            else:
                left[i] = right[i - 1] + 1
            while left[i] <= i and right[i - 1] <= i and (product_so_far[i - 1] % product == 0):
                right[i] = min(i + length, right[i - 1])
                product_so_far[i] = product_so_far[i - 1] // product * arr[i] if product_so_far[i - 1] // product * arr[i] != 0 else 1
            if product_so_far[i] == product:
                yield arr[left[i]:right[i]]
    return list(find_subarrays(circular_list, 99))