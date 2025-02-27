def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 22):
        substring = text[i:i + 23].lower()
        if substring == substring[::-1] and len(substring) >= 23:
            palindromes.add(text[i:i + 23])
    return palindromes