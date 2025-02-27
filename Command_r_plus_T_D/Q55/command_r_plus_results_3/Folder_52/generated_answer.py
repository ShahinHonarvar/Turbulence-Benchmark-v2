def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target_product, size):
        for i in range(len(lst)):
            for j in range(i, min(i + size, len(lst))):
                if product(lst[i:j + 1]) == target_product:
                    yield lst[i:j + 1]

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    sublists = []
    for size in range(1, len(circular_list) + 1):
        sublists.extend(find_subarrays(circular_list, 37, size))
    return sublists