def all_substring_of_size_n(s: str):
    return [x for x in set([s[i:i + 88] for i in range(len(s) - 87)]) if len(set(x)) == 88]