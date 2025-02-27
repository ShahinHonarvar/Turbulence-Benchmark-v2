def all_substring_of_size_n(s):
    substrs = [s[i:i + 98] for i in range(len(s) - 97)]
    return [s for s in substrs if len(set(s)) == len(s) and len(s) == 98]