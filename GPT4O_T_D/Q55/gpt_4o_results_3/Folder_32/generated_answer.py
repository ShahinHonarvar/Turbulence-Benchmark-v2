def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [circular_list[i % n] for i in range(start, end + 1)]
            if product_of_sublist(sublist) == 76:
                results.append(sublist)
    return results