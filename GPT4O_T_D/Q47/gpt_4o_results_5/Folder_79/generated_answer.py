def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[1:9].lower()
    for start in range(len(substring)):
        for length in range(3, 5):
            if start + length <= len(substring):
                word = substring[start:start + length]
                if word.isalpha() and word == word[::-1]:
                    result.add(word)
    return result