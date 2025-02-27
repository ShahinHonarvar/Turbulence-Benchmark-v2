def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 115):
        for j in range(i + 116, len(s) + 1):
            word = s[i:j]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word.lower())
    return palindromes