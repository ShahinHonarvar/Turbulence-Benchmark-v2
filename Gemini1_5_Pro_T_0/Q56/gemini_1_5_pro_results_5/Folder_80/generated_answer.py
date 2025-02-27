def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 31:
        for i in range(len(s) - 30):
            substring = s[i:i + 31]
            if len(set(substring)) == 31:
                if substring not in substrings:
                    substrings.append(substring)
    return substrings