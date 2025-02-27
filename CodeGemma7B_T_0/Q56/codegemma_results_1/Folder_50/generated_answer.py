def all_substring_of_size_n(text):
    result = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if len(set(text[i:j + 1])) == 11:
                result.add(text[i:j + 1])
    return list(result)