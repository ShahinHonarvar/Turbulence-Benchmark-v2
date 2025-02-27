def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 275):
        substring = text[i:i + 276]
        if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes