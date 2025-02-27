def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 27):
        substring = text[i:i + 28].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 28])
        for j in range(i + 29, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha() and (len(substring) >= 28):
                result.add(text[i:j])
    return result