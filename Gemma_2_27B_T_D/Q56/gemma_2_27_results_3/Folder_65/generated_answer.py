def all_substring_of_size_n(s):
    return [s[i:i + 81] for i in range(len(s) - 80) if len(set(s[i:i + 81])) == 81]