def all_substring_of_size_n(text):
    d = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if len(text[i:j + 1]) == 10 and len(set(text[i:j + 1])) == len(text[i:j + 1]):
                d.add(text[i:j + 1])
    return list(d)