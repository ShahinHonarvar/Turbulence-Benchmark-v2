def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 24):
        substring = text[i:i + 25].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
        for j in range(i + 26, len(text) + 1):
            substring = text[i:j].lower()
            if substring == substring[::-1] and substring.isalpha() and (len(substring) >= 25):
                palindromes.add(substring)
    return palindromes