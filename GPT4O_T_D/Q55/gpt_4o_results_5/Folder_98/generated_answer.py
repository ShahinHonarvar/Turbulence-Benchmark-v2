def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def calculate_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    for start_index in range(n):
        for size in range(1, n + 1):
            sublist = []
            for i in range(size):
                index = (start_index + i) % n
                sublist.append(circular_list[index])
            if calculate_product(sublist) == -1:
                result.append(sublist)
    return result