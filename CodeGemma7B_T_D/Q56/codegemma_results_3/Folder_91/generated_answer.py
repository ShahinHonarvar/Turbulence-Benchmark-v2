def all_substring_of_size_n(text):
    lst = []
    for i in range(len(text) - 5):
        j = i + 6
        lst.append(text[i:j])
    return list(set(lst))