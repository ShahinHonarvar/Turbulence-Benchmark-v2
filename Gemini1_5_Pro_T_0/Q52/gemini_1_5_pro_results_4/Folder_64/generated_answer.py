def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 8):
        substring = text[i:i + 9]
        if substring.lower() == substring.lower()[::-1] and len(substring) == 9 and substring.isalpha():
            palindromes.add(substring.lower())
    return palindromes