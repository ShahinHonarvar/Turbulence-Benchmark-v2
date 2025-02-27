def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    if not circular_list:
        return []
    product_78 = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and calculate_product(sublist) == 78:
                product_78.append(sublist)
    return product_78

def calculate_product(lst: list[int]) -> int:
    product = 1
    for num in lst:
        product *= num
    return product