def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 65):
        substring = text[i:i + 66]
        if len(substring) == 66 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes