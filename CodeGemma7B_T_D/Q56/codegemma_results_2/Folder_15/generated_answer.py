def all_substring_of_size_n(text):
    result = set()
    for a in range(len(text)):
        for b in range(a, len(text)):
            if b - a == 2:
                word = text[a:b + 1]
                result.add(word)
    return list(result)