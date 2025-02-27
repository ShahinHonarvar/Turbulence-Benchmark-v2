def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    n = -906
    length = len(circular_list)
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, i + length):
            index = j % length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist)
                product = 1
                sublist = []
    return result