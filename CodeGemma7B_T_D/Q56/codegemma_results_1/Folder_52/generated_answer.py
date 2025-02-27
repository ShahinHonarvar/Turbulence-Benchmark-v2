def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 14):
        substring = text[i:i + 15]
        if len(set(substring)) == 15:
            result.append(substring)
    return result