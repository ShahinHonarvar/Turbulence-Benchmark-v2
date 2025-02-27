def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 474):
        for j in range(i + 1, len(text) - 473):
            temp = text[i:j + 475]
            if temp == temp[::-1] and temp.isalpha():
                result.add(temp.lower())
    return result