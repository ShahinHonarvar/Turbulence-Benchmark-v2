def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 12):
        substring = text[i:i + 13]
        if substring.lower() == substring.lower()[::-1] and len(substring) == 13 and substring.isalpha():
            palindromes.add(substring.lower())
    return palindromes