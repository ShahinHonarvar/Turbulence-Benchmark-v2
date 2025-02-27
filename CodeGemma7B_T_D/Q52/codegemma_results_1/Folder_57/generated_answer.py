def palindrome_of_length_n(word):
    word_lower = word.lower()
    palindromes = set()
    for i in range(len(word_lower)):
        for j in range(i + 2, len(word_lower) + 2):
            substring = word_lower[i:j]
            if substring == substring[::-1]:
                if len(substring) == 92:
                    palindromes.add(substring)
    return palindromes