def all_substring_of_size_n(s):
    substr = [s[i:i + 106] for i in range(len(s) - 105)]
    return [s for s in substr if len(set(s)) == len(s)]