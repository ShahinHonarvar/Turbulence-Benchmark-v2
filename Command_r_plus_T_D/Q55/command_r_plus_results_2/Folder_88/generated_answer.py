def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, target, size):
        subarrays = []
        for i in range(len(lst)):
            for j in range(i, min(i + size, len(lst))):
                if prod(lst[i:j + 1]) == target:
                    subarrays.append(lst[i:j + 1])
        return subarrays

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = -56
    size = len(circular_list)
    sublists = []
    for i in range(size):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], n, size)
        sublists.extend(subarrays)
    return sublists