from re import finditer

def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 16):
        for j in range(i + 1, len(text)):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes