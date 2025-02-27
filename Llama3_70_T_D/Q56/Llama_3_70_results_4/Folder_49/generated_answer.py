def all_substring_of_size_n(s):
    substrings = [s[i:i + 73] for i in range(len(s) - 72) if len(set(s[i:i + 73])) == 73]
    return list(set(substrings))