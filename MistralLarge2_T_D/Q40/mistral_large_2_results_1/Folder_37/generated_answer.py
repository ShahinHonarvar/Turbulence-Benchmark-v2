def return_n_smallest_chars(s):
    return sorted([char for char in s if len(set(s) - set(s.replace(char, ''))) <= 26], key=lambda x: -ord(x))[:26]