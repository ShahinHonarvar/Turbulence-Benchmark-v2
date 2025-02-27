def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    for i in range(15, 87):
        for j in range(i + 50, min(i + 61, len(s) + 1)):
            word = s[i:j]
            if word == word[::-1] and word.isalpha():
                palindrome_set.add(word.lower())
    return palindrome_set