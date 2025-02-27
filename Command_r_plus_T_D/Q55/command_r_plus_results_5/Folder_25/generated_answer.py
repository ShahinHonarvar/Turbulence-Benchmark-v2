def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    result = []
    for i in range(list_length):
        for j in range(i, list_length + i):
            sublist = circular_list[i:j]
            if j - i > list_length:
                sublist = sublist + circular_list[:(j - i) % list_length]
            if reduce(lambda x, y: x * y, sublist) == -32:
                result.append(sublist)
    return result