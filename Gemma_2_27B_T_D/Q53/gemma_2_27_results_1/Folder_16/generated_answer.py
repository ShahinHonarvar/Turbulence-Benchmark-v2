def palindrome_of_length_at_least_n(text):
    result = set()
    for i in range(len(text) - 118):
        substring = text[i:i + 119].lower()
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result