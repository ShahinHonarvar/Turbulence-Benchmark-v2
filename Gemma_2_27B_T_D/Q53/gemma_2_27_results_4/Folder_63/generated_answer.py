def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 36):
        substring = text[i:i + 37].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(text[i:i + 37])
    return palindromes