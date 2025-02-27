def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 60):
        substring = text[i:i + 61]
        if len(set(substring)) == 61:
            result.append(substring)
    return result