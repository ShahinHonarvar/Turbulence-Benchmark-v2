def all_substring_of_size_n(s):
    all_substrings = []
    for i in range(len(s)):
        for j in range(i + 97, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == 97 and substring not in all_substrings:
                all_substrings.append(substring)
    return all_substrings