def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 12):
        substring = text[i:i + 13].lower()
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes