def palindrome_of_length_n(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 278):
        for j in range(i + 279, len(text)):
            temp = text[i:j + 1]
            if temp == temp[::-1]:
                result.add(temp)
    return result