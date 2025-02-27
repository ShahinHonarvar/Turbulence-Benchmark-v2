def all_substring_of_size_n(s):
    all_substrings = [s[i:i + 105] for i in range(len(s) - 104)]
    distinct_substrings = [sub for sub in all_substrings if len(set(sub)) == 105]
    return distinct_substrings