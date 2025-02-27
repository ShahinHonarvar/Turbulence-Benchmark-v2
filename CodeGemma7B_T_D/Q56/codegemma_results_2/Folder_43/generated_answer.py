def all_substring_of_size_n(text):
    result = set()
    for i in range(len(text) - 85):
        substring = text[i:i + 86]
        if len(set(substring)) == 86:
            result.add(substring)
    return sorted(list(result))