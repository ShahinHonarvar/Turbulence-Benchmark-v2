def palindromes_of_specific_lengths(s):
    s = s[11:88]
    palindromes = set()
    for length in range(4, 6):
        for i in range(0, len(s) - length + 1):
            word = s[i:i + length]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word.lower())
    return palindromes