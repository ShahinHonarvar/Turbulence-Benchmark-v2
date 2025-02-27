def palindrome_of_length_at_least_n(word):
    word = word.lower()
    palindromes = set()
    for i in range(len(word) - 89):
        for j in range(i + 99, len(word)):
            if word[i:j + 1] == word[i:j + 1][::-1]:
                palindromes.add(word[i:j + 1])
    return palindromes