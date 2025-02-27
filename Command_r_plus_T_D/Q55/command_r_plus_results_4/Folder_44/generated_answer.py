def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    n = 29
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and prod(sublist) == n:
                result.append(sublist)
    return result

def prod(lst: list[int]) -> int:
    product = 1
    for num in lst:
        product *= num
    return product