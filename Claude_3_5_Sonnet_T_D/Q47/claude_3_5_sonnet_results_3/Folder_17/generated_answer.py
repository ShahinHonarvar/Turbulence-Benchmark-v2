def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[22:96]
    for i in range(len(substring)):
        for length in range(52, 56):
            if i + length <= len(substring):
                word = substring[i:i + length]
                if word.isalpha():
                    if word.lower() == word.lower()[::-1]:
                        result.add(word)
    return result