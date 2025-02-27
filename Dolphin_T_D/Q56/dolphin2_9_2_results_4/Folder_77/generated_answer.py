def all_substring_of_size_n(n):
    substrings = set()
    string_length = len(n)
    is_substring_valid = [False for _ in range(string_length - 143)]
    for i in range(string_length - 143):
        sub_string = n[i:i + 144]
        if len(set(sub_string)) == 144:
            substrings.add(sub_string)
            is_substring_valid[i] = True
    if len(substrings) == 0:
        return []
    return list(substrings)