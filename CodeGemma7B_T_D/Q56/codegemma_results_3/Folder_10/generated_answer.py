def all_substring_of_size_n(text):
    return [''.join(i) for i in product(set(text), repeat=n)]