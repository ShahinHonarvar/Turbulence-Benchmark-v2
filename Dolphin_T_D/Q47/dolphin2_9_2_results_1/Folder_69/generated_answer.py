def palindromes_of_specific_lengths(s):
    s = s[10:97]
    palindromes = set()
    for length in range(45, 53):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if word == word.lower() and word == word[::-1].lower():
                palindromes.add(word)
    return palindromes