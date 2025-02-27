def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product, start, end):
        if start > end:
            return []
        if end - start + 1 == product:
            return [arr[start:end + 1]]
        subarrays = []
        for i in range(start, end + 1):
            subarrays += find_subarrays(arr, product, start, i - 1)
            subarrays += find_subarrays(arr, product, i + 1, end)
        return subarrays

    def find_circular_subarrays(arr, product):
        n = len(arr)
        subarrays = []
        for i in range(n):
            subarrays += find_subarrays(arr, product, i, i + product - 2)
        return subarrays
    product_target = -1
    if any((num == 0 for num in circular_list)):
        return []
    if product_target == 1:
        return [[]]
    result = find_circular_subarrays(circular_list, len(circular_list)) + find_circular_subarrays(circular_list + circular_list, len(circular_list))
    result = [sublist for sublist in result if -1 in [prod for prod in [1] * (len(sublist) - 1) if all((sublist[i] * sublist[i + 1] == prod for i in range(len(sublist) - 1)))]]
    return result