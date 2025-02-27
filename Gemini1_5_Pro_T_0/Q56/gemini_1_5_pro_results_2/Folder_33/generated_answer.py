def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 105:
        for i in range(len(s) - 104):
            substring = s[i:i + 105]
            if len(set(substring)) == 105:
                if substring not in substrings:
                    substrings.append(substring)
    return substrings