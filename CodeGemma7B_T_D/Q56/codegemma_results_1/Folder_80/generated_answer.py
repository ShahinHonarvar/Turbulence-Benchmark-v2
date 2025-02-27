def all_substring_unique(text):
    result = []
    for i in range(len(text) - 30):
        substring = text[i:i + 31]
        if len(set(substring)) == 31 and substring not in result:
            result.append(substring)
    return result