def palindrome_of_length_n(english_text):
    n = 72
    english_text = english_text.lower()
    palindromes = set()
    for i in range(len(english_text) - n + 1):
        substring = english_text[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes