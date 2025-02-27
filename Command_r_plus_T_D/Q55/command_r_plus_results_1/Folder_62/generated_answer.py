def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    n = 100
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and n % prod(sublist) == 0:
                result.append(sublist)
    return result

def prod(lst: list[int]) -> int:
    result = 1
    for num in lst:
        result *= num
    return result