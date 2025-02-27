def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 79):
        substring = text[i:i + 80]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes