def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 91):
        substring = text[i:i + 92].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(text[i:i + 92])
    return palindromes