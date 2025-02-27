def palindrome_of_length_n(word):
    word = word.lower()
    palindromes = set()
    for i in range(len(word) - 17):
        for j in range(i + 1, len(word)):
            substring = word[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes