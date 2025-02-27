def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, target_product, start, end):
        if start > end:
            return []
        if end - start + 1 < len(circular_list):
            return []
        product_so_far = 1
        for i in range(start, end + 1):
            product_so_far *= array[i % len(array)]
            if product_so_far == target_product:
                yield array[start:i + 1]
            if product_so_far == target_product * -1:
                break
    result = []
    for i in range(len(circular_list)):
        for subarray in find_subarrays(circular_list, -65, i, i + len(circular_list) - 1):
            result.append(subarray)
    return result