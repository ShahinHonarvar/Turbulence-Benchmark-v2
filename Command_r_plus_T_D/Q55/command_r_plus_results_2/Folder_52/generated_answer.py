def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:
    result = []
    n = 37
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if len(sublist) <= len(circular_list) and sublist[-1] * sublist[0] <= n:
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    result.append(sublist)
    return result