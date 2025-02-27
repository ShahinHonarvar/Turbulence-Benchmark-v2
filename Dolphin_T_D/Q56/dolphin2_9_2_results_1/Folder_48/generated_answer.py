def all_substring_of_size_n(word):
    result = []
    for i in range(len(word)):
        if len(set(word[i:i + 120])) == 120:
            result.append(word[i:i + 120])
    return result