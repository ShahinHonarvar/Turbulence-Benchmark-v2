def all_substring_of_size_n(text):
    if len(text) < 19:
        return []
    result = set()
    for i in range(len(text) - 18):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if len(set(substring)) == len(substring):
                result.add(substring)
    return list(result)