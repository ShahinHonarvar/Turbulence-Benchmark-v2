def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(start, product):
        subarrays = []
        curr_product = 1
        for i in range(start, len(circular_list) + start):
            index = i % len(circular_list)
            curr_product *= circular_list[index]
            if curr_product == product:
                subarrays.append(circular_list[start:i + 1])
            if curr_product > product or i == len(circular_list) + start - 1:
                break
        return subarrays
    product = 851
    sublists = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(i, product)
        sublists.extend(subarrays)
    return sublists