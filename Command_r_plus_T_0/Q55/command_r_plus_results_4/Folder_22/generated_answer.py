def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if product(arr[i:j + 1]) == product:
                    subarrays.append(arr[i:j + 1])
        return subarrays

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    sublists = find_subarrays(circular_list, 4)
    sublists.extend(find_subarrays(circular_list[::-1], 4))
    unique_sublists = []
    for sublist in sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    return unique_sublists