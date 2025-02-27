def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 47):
        substring = text[i:i + 48].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result