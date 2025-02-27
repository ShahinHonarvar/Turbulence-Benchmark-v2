def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 77):
        substring = text[i:i + 78].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 78])
    return result