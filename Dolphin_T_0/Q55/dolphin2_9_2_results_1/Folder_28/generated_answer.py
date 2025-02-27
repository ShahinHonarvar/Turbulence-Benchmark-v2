def lists_with_product_equal_n(lst):

    def get_sublists(lst):
        for length in range(1, len(lst) + 1):
            for i in range(len(lst)):
                product = 1
                for j in range(i, i + length):
                    product *= lst[j % len(lst)]
                    if product == 85:
                        yield lst[i:i + length]
    return list(get_sublists(lst))