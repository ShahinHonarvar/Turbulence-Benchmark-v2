def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(target_product, array):
        result = []
        for i in range(len(array)):
            product = 1
            for j in range(i, len(array)):
                product *= array[j]
                if product == target_product:
                    result.append(array[i:j + 1])
                if product > target_product:
                    break
        return result
    result = []
    for i in range(len(circular_list)):
        rotated_list = circular_list[i:] + circular_list[:i]
        result.extend(find_subarrays(28, rotated_list))
    return result