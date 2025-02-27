def all_substring_of_size_n(string):
    n = 127
    size = len(string)
    substr = [string[i:i + n] for i in range(size - n + 1)]
    unique_substr = list(set(substr))
    return [s for s in unique_substr if len(set(s)) == n]