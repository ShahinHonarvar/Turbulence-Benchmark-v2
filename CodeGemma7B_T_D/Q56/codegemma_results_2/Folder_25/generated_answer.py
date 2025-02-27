def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 66):
        substring = text[i:i + 67]
        if len(set(substring)) == 67:
            result.append(substring)
    return result