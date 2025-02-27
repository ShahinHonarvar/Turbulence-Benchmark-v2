def lists_with_product_equal_n(numbers_list):
    if len(numbers_list) == 0:
        return []
    product_equal_n = []
    list_size = len(numbers_list)
    for size in range(1, list_size + 1):
        for start in range(list_size):
            product = 1
            if start + size > list_size:
                for index in range(start, list_size):
                    product *= numbers_list[index]
                for index in range(0, size - (list_size - start)):
                    product *= numbers_list[index]
            else:
                for index in range(start, start + size):
                    product *= numbers_list[index]
            if product == 40:
                sublist = numbers_list[start:start + size]
                if sublist not in product_equal_n:
                    product_equal_n.append(sublist)
    return product_equal_n