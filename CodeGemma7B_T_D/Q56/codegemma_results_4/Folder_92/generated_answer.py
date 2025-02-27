def all_substring_of_size_n(text):
    result = []
    if len(text) < 9:
        return result
    for i in range(len(text) - 8):
        substring = text[i:i + 9]
        if len(set(substring)) == 9:
            result.append(substring)
    return result