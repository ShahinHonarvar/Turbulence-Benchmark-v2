def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 55):
        substring = text[i:i + 56]
        if len(substring) == 56 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes