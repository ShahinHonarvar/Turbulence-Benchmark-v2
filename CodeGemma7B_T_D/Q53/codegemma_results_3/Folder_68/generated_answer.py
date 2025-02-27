def palindrome_of_length_at_least_n(text):
    all_palindromes = set()
    lower_text = text.lower()
    for i in range(len(lower_text)):
        for j in range(i + 1, len(lower_text) + 1):
            substring = lower_text[i:j]
            if substring == substring[::-1] and len(substring) >= 21:
                all_palindromes.add(substring)
    return all_palindromes