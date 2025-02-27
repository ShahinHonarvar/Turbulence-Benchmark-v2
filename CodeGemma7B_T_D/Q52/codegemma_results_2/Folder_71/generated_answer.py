def palindrome_of_length_n(word):
    word = word.lower()
    palindromes = set()
    for i in range(len(word)):
        for j in range(i + 78, len(word) + 1):
            if word[i:j] == word[j - 78:j][::-1]:
                palindromes.add(word[i:j])
    return palindromes