def lists_with_product_equal_n(circular_list):

    def product_of_list(l):
        product = 1
        for num in l:
            product *= num
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [circular_list[i % n] for i in range(start, end + 1)]
            if product_of_list(sublist) == 46:
                results.append(sublist)
    return results