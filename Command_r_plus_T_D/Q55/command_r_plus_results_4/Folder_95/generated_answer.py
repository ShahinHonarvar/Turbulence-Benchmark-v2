def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start, product):
        subarrays = []
        current_product = 1
        current_sublist = []
        for i in range(start, len(circular_list) + start):
            index = i % len(circular_list)
            current_product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if current_product == product:
                subarrays.append(current_sublist.copy())
                current_sublist.pop(0)
                current_product //= circular_list[index - 1]
        return subarrays
    sublists = []
    product = 28
    for i in range(len(circular_list)):
        subarrays = find_subarrays(i, product)
        sublists.extend(subarrays)
    return sublists