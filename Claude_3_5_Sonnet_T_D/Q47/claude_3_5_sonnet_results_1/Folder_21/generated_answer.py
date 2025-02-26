def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:296]
    for i in range(len(substring)):
        for j in range(i + 136, min(i + 161, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                result.add(word)
    return result