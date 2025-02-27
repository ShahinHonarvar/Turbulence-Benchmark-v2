def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(12, 21):
        substring = s[29:85]
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word.lower() == word[::-1].lower() and word.isalpha():
                result.add(word)
    return result