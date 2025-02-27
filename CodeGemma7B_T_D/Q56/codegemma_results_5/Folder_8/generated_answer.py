def all_substring_of_size_n(text):
    result = []
    for i in range(len(text) - 29):
        substring = text[i:i + 30]
        if len(set(substring)) == 30 and substring not in result:
            result.append(substring)
    return result