def all_substring_of_size_n(s):
    if len(set(s)) != 26 or len(s) != 26:
        return []
    return list(map(''.join, zip(*[iter(s)] * 26)))