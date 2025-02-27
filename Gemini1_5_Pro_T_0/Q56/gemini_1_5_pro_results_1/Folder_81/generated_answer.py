def all_substring_of_size_n(s):
    substrings = []
    if len(s) >= 98:
        for i in range(len(s) - 97):
            substring = s[i:i + 98]
            if len(set(substring)) == 98:
                if substring not in substrings:
                    substrings.append(substring)
    return substrings