def palindrome_of_length_at_least_n(text):
    text = text.lower()
    alphanumeric = 'abcdefghijklmnopqrstuvwxyz'
    valid_palindrome = set()
    for i in range(len(text)):
        for j in range(i + 48, len(text)):
            if text[i] == text[j] and all((char in alphanumeric for char in text[i + 1:j])):
                valid_palindrome.add(text[i:j + 1])
    return valid_palindrome