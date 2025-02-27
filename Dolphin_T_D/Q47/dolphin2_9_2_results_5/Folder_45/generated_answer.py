def palindromes_of_specific_lengths(s):
    substring = s[70:141]
    palindromes = set()
    for length in range(3, 61):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word.lower())
    return palindromes