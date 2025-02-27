def all_substring_of_size_n(text):
    if len(text) < 28:
        return []
    result = set()
    for i in range(len(text) - 27):
        result.add(text[i:i + 28])
    return list(result)