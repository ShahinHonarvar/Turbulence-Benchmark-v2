def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product):
        length = len(arr)
        left, right = ([0] * length, [length] * length)
        product = [1] * length
        for i in range(length):
            product[i] = product[i - 1] * arr[i] if i else 1
        for i in range(length):
            for j in range(i, length):
                if product[j] % target_product == 0 and product[i - 1] == product[j] // target_product:
                    left[j], right[i] = (i, j + 1)
        result = []
        for i in range(length):
            if product[i] % target_product == 0:
                result.append(arr[left[i]:right[i]])
        return result
    sublists = find_subarrays(circular_list, -15)
    sublists_with_duplicates = []
    for sublist in sublists:
        if -15 in [reduce(lambda x, y: x * y, sublist[i:j]) for i in range(len(sublist)) for j in range(i + 1, len(sublist) + 1)]:
            sublists_with_duplicates.append(sublist)
    return sublists_with_duplicates