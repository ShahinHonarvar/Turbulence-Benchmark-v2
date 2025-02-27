def all_substring_of_size_n(text):
    length = 68
    result = set()
    for i in range(len(text) - length + 1):
        substring = text[i:i + length]
        if len(set(substring)) == length:
            result.add(substring)
    return list(result)