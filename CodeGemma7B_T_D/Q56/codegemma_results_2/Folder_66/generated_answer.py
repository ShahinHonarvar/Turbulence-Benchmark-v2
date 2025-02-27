def all_substring_of_size_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if len(substring) == 26 and len(set(substring)) == 26:
                result.add(substring)
    return list(result)