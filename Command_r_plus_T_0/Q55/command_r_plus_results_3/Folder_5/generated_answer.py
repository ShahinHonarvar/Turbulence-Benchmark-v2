def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 == arr.count(1):
            return [arr[start:end + 1]]
        subarrays = []
        product = 1
        for i in range(start, end + 1):
            product *= arr[i]
            if product == target_product:
                subarrays.append(arr[start:i + 1])
            if product > target_product and i - start > 1:
                subarrays.extend(find_subarrays(arr, target_product, start, i - 1))
            if product * arr[i + 1] > target_product and end - i > 1:
                subarrays.extend(find_subarrays(arr, target_product, i + 1, end))
        return subarrays
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j] + circular_list[i:][j - i:]
            if len(sublist) <= len(circular_list) and -33 in [reduce(lambda x, y: x * y, sublist[i:j]) for i, j in enumerate(range(len(sublist) + 1))]:
                result.append(sublist)
    return result