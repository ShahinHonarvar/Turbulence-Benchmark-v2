def palindrome_of_length_at_least_n(text):
    low_text = text.lower()
    set_of_palindromes = set()
    for i in range(len(low_text)):
        for j in range(i, len(low_text)):
            substring = low_text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 34:
                set_of_palindromes.add(substring)
    return set_of_palindromes