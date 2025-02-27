def all_substring_of_size_n(text):
    while len(text) % 29 != 0:
        text = text + '.'
    list = []
    for i in range(0, len(text), 29):
        list.append(text[i:i + 29])
    return list