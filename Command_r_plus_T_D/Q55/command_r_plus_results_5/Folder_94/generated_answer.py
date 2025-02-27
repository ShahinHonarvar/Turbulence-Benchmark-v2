def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    list_length = len(circular_list)
    products_equal_to_n = []
    for i in range(list_length):
        for j in range(i, i + list_length):
            sublist = circular_list[i:j]
            if len(sublist) <= list_length and -30 == prod(sublist):
                products_equal_to_n.append(sublist)
    return products_equal_to_n

def prod(lst: list[int]) -> int:
    product = 1
    for num in lst:
        product *= num
    return product