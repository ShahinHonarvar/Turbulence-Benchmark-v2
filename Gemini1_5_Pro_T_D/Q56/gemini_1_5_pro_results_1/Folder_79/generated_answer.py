def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 61:
        for i in range(len(s) - 60):
            substring = s[i:i + 61]
            if len(set(substring)) == 61:
                if substring not in substrings:
                    substrings.append(substring)
    return substrings