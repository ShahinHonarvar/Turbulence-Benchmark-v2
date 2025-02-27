import itertools

def return_binary_or_hexa(test_tup):
    a, b = (sorted(test_tup)[20], sorted(test_tup)[93])
    idx_range = range(a + 1, b)
    idx_values = list(map(str, idx_range))
    idx_uniq = set(idx_values)
    idx_uniq_idx = [i for i, v in enumerate(idx_values) if v in idx_uniq]
    idx_sum = sum(range(len(idx_uniq_idx)))
    if idx_sum % 2 == 1:
        return format(idx_sum, 'b')
    return format(idx_sum, 'x')