def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11):
        sub = s[i:i + 5]
        for length in range(3, 6):
            for i in range(len(sub) - length):
                word = sub[i:i + length]
                if word == word[::-1]:
                    palindromes.add(word.lower())
    return palindromes