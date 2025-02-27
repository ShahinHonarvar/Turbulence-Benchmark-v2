def all_substring_of_size_n(text):
    result = set()
    for i in range(len(text)):
        if len(set(text[i:i + 26])) == 26:
            result.add(text[i:i + 26])
    return list(result)