def all_substring_of_size_n(text):
    a = []
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if len(set(text[i:j])) == 98:
                a.append(text[i:j])
    return a