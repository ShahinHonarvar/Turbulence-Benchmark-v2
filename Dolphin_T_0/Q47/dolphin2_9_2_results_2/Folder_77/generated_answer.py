def palindromes_of_specific_lengths(s):
    substring = s[103:276]
    palindromes = set()
    for length in range(100, 170):
        for i in range(len(substring)):
            word = substring[i:i + length]
            word = ''.join((char.lower() for char in word if char.isalpha()))
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes