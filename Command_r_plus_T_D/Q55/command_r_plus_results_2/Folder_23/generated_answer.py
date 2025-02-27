def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_subarrays(arr: list[int], target_product: int) -> list[list[int]]:
        result = []
        n = len(arr)
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= arr[j]
                if product == target_product:
                    result.append(arr[i:j + 1])
                if product > target_product:
                    break
        return result
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        result.extend(find_product_subarrays(sublist, -95))
    return result