def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 56):
        substring = text[i:i + 57].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(text[i:i + 57])
    return result