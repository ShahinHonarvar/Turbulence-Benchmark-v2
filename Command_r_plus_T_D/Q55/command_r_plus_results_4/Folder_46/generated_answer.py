def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_53(start_index, product_so_far=1):
        for i in range(start_index, len(circular_list) + start_index):
            index = i % len(circular_list)
            product_so_far *= circular_list[index]
            if product_so_far == 53:
                return [circular_list[j % len(circular_list)] for j in range(start_index, i + 1)]
            elif product_so_far > 53:
                break
        return []
    result = []
    for i in range(len(circular_list)):
        sublist = find_product_53(i)
        if sublist:
            result.append(sublist)
    return result