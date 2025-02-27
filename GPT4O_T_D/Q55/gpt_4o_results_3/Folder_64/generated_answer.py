def lists_with_product_equal_n(circular_list):

    def adjacent_products(lst, size):
        result = []
        for start in range(len(lst)):
            product = 1
            for end in range(start, start + size):
                product *= lst[end % len(lst)]
                if product == 3:
                    sublist = [lst[i % len(lst)] for i in range(start, end + 1)]
                    result.append(sublist)
        return result
    n = len(circular_list)
    all_sublists = []
    for length in range(1, n + 1):
        all_sublists.extend(adjacent_products(circular_list, length))
    return all_sublists