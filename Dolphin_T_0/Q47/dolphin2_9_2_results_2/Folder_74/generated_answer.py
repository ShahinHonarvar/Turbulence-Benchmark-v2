def palindromes_of_specific_lengths(s):
    s = s[30:85]
    palindrome_set = set()
    for length in range(12, 21):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if word.lower() == word.lower()[::-1] and word.isalpha():
                palindrome_set.add(word)
    return palindrome_set