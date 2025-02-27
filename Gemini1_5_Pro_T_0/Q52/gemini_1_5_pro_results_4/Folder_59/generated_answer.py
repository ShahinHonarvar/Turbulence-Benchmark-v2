def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 38):
        substring = text[i:i + 39]
        if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes