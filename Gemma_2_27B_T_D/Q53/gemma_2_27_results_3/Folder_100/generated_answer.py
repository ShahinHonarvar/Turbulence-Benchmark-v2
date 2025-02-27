def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 47):
        substring = text[i:i + 48].lower()
        if substring == substring[::-1] and len(substring) >= 48:
            palindromes.add(text[i:i + 48])
    return palindromes