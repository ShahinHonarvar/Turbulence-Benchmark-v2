def palindromes_of_specific_lengths(s):
    substring = s[11:88]
    result = set()
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length <= len(substring):
                word = substring[i:i + length]
                if word.isalpha() and word.lower() == word.lower()[::-1]:
                    result.add(word.lower())
    return result