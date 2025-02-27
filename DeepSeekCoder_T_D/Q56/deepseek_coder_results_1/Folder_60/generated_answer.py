def all_substring_of_size_n(s):

    def is_valid(sub):
        return len(set(sub)) == len(sub)
    n = 36
    return [s[i:i + n] for i in range(len(s) - n + 1) if is_valid(s[i:i + n])]