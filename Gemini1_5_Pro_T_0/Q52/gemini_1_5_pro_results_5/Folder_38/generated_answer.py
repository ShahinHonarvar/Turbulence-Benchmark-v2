def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 37):
        substring = text[i:i + 38]
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes