def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 == arr.__len__() and target_product == 1:
            return [arr]
        result = []
        for i in range(start, end + 1):
            product = 1
            temp = []
            for j in range(i, end + 1):
                product *= arr[j % arr.__len__()]
                temp.append(arr[j % arr.__len__()])
                if product == target_product:
                    result.append(temp)
        return result
    target_product = -76
    subarrays = find_subarrays(circular_list, target_product, 0, circular_list.__len__() - 1)
    return subarrays