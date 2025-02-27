def palindromes_of_specific_lengths(s):
    palindrome = set()
    for i in range(31, 75):
        for j in range(23, 40):
            word = s[i - j:i + j + 1]
            if word == word[::-1] and word.isalpha() and (word.lower() not in palindrome):
                palindrome.add(word.lower())
    return palindrome