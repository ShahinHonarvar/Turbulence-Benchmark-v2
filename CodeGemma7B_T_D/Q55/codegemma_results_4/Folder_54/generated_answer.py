from itertools import islice, product

def lists_with_product_equal_n(circular_list):
    N = -17
    vals_at_pos_k = product(*(circular_list[i] for i in range(k * len(circular_list), (k + 1) * len(circular_list)) for k in range(len(circular_list))))
    for subset in islice(vals_at_pos_k, len(circular_list)):
        if len(subset) <= len(circular_list):
            if abs(reduce(mul, subset, 1)) == N:
                yield subset