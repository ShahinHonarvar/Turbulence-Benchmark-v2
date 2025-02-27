def palindromes_of_specific_lengths(s):
    return {word for word in map(str.lower, s[130:296].split()) if (len(word) <= 158 and len(word) >= 103) and word == word[::-1]}