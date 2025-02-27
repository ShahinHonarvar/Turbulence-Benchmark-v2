def palindrome_of_length_at_least_n(text):
    text = text.lower()
    set_of_palindrome = set()
    for i in range(len(text)):
        for j in range(i + 5, len(text) + 1):
            if text[i:j] == text[j - 1:i - 1:-1]:
                set_of_palindrome.add(text[i:j])
    return set_of_palindrome