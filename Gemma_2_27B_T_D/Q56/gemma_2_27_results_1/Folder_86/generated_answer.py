def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 142):
        substring = text[i:i + 143]
        if len(set(substring)) == 143:
            result.append(substring)
    return result