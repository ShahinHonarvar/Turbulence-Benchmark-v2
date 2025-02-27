def palindrome_of_length_n(english_text):
    n = 472
    palindromes = set()
    for i in range(len(english_text) - n + 1):
        substring = english_text[i:i + n].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes