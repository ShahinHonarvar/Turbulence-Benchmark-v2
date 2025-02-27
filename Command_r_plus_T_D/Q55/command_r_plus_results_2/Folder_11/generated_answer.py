def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_product_sublists(product, circular_list):
        length = len(circular_list)
        for i in range(length):
            for j in range(i, length + i):
                sublist = circular_list[j % length:j % length + i + 1]
                if len(sublist) > length:
                    continue
                if product(sublist) == -15:
                    yield sublist
    product_func = lambda lst: -15 if lst else 1
    return list(find_product_sublists(product_func, circular_list))