def palindrome_of_length_n(text):
    result = set()
    for i in range(len(text) - 12):
        substring = text[i:i + 13].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 13])
    return result