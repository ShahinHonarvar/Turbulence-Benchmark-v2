def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 9):
        substring = text[i:i + 10]
        if len(set(substring)) == 10:
            result.append(substring)
    return result