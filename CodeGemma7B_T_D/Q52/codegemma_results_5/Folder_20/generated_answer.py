def palindrome_of_length_n(text):
    seen_palindrome = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            substr = text[i:j + 1]
            if substr == substr[::-1] and substr.isalpha():
                seen_palindrome.add(substr.lower())
    return seen_palindrome