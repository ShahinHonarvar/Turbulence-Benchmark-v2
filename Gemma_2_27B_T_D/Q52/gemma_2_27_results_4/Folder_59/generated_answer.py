def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 38):
        substring = text[i:i + 39].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 39])
    return result