def all_substring_of_size_n(str):
    substrings = []
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            substring = str[i:j + 1]
            if len(substring) == 77:
                substrings.append(substring)
    distinct_substrings = []
    for substring in substrings:
        if substring not in distinct_substrings:
            distinct_substrings.append(substring)
    return distinct_substrings