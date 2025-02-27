def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 75):
        substring = text[i:i + 76]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes