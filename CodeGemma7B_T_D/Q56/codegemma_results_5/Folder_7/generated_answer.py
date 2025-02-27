import itertools

def all_substring_of_size_n(str_len):
    if len(str_len) < 117:
        return []
    a = list(str_len)
    return [''.join(i) for i in itertools.product(a, repeat=117) if len(set(i)) == len(i)]