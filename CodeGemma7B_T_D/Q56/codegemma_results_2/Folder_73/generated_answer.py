def all_substring_of_size_n(text):
    result = set()
    for i in range(len(text) - 19 + 1):
        substring = text[i:i + 20]
        if len(set(substring)) == 20:
            result.add(substring)
    return list(result)