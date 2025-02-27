def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 2):
        substring = text[i:i + 3].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes