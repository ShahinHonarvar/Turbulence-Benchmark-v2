def lists_with_product_equal_n(lst):

    def generate_product(lst, n):
        product = 1
        start_idx = 0
        sublists = []
        for end_idx in range(len(lst)):
            product *= lst[end_idx]
            while product > n:
                product /= lst[start_idx]
                start_idx += 1
            if product == n:
                sublists.append(lst[start_idx:end_idx + 1])
        return sublists
    circular_lst = lst + lst[:1]
    return generate_product(circular_lst, 78)