def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 15:
        for i in range(len(s) - 14):
            substring = s[i:i + 15]
            if len(set(substring)) == 15:
                if substring not in substrings:
                    substrings.append(substring)
    return substrings