def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 39):
        substring = text[i:i + 40].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 40])
    return result