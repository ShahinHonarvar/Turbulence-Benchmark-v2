def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 86):
        substring = text[i:i + 87].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes