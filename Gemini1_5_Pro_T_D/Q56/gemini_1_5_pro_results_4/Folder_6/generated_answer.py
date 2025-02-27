def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 23:
        for i in range(len(s) - 22):
            substring = s[i:i + 23]
            if len(set(substring)) == 23:
                if substring not in substrings:
                    substrings.append(substring)
    return substrings