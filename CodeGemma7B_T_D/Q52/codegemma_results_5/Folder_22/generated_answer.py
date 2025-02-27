def palindrome_of_length_n(text):
    lst = list()
    text = text.lower()
    for i in range(len(text) - 20 + 1):
        for j in range(i + 21, len(text)):
            if text[i:j] == text[i:j][::-1]:
                lst.append(text[i:j])
    return set(lst)