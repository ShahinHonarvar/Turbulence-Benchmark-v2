def palindrome_of_length_n(text):
    text = text.lower()
    lst = []
    for i in range(len(text) - 87):
        for j in range(i + 1, len(text) - 87):
            for k in range(j + 1, len(text) - 87):
                for l in range(k + 1, len(text) + 1):
                    print(text[i:k], text[j:l])
                    if text[i:k] == text[j:l][::-1] and text[i:k].isalpha() and text[j:l].isalpha():
                        lst.append(text[i:k])
    return set(lst)