def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i] == text[j]:
                current_palindrome = text[i:j + 1]
                if len(current_palindrome) >= 74:
                    palindromes.add(current_palindrome)
    return palindromes