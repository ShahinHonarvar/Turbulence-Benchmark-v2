def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(array, target, n):
        result = []
        for i in range(len(array)):
            product = 1
            subarray = []
            for j in range(i, min(i + n, len(array))):
                product *= array[j]
                subarray.append(array[j])
                if product == target:
                    result.append(subarray)
        return result
    sublists = find_subarrays(circular_list, 100, len(circular_list))
    circular_sublist = circular_list + circular_list
    sublists += find_subarrays(circular_sublist, 100, len(circular_list))
    return sublists