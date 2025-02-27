def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_sublists(circular_list):
        n = len(circular_list)
        sublists = []
        for length in range(1, n + 1):
            for i in range(n):
                sublist = [circular_list[(i + j) % n] for j in range(length)]
                sublists.append(sublist)
        return sublists
    sublists = get_sublists(circular_list)
    result = [sublist for sublist in sublists if product(sublist) == -22]
    return result