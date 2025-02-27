def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 42):
        substring = text[i:i + 43]
        if len(set(substring)) == 43:
            result.append(substring)
    return result