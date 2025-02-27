def palindrome_of_length_n(string, length=464):
    english_letters = set((string.upper() if string.isalpha() else '' for string in string))
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring.upper() == substring.upper()[::-1] and set(substring) <= english_letters:
            palindromes.add(substring)
    return palindromes