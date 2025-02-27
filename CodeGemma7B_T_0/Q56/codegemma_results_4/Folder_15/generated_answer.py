def all_substring_of_size_n(text):
    if len(text) < 3:
        return []
    result = set()
    for i in range(len(text) - 2):
        for j in range(i + 1, len(text) - 1):
            for k in range(j + 1, len(text)):
                substring = text[i:k + 1]
                if len(substring) == len(set(substring)):
                    result.add(substring)
    return list(result)