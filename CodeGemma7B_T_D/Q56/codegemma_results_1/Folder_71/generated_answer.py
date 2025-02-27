def all_substring_of_size_n(text):
    result = []
    if len(text) < 17:
        return result
    for i in range(len(text) - 16):
        substring = text[i:i + 17]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result