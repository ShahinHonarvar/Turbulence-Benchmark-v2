def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(lst, product):
        length = len(lst)
        for i in range(length):
            for j in range(i, length):
                if product(lst[i:j + 1]) == n:
                    yield lst[i:j + 1]
    n = 733
    product = lambda lst: eval('*'.join(map(str, lst)))
    result = []
    for sublist in find_subarrays(circular_list, product):
        result.append(sublist)
    return result