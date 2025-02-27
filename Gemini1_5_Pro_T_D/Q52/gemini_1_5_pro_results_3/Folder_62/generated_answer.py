def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 187):
        substring = text[i:i + 188]
        if substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes