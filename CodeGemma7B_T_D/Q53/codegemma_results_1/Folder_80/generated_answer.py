def palindrome_of_length_at_least_n(text):
    unique_palindrome = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 2, len(text)):
            if text[i] == text[j]:
                if text[i:j + 1] == text[i:j + 1][::-1] and len(text[i:j + 1]) >= 30:
                    unique_palindrome.add(text[i:j + 1])
    return unique_palindrome