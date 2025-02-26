def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[75:96]
    for i in range(len(substring)):
        for j in range(i + 7, min(i + 10, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                result.add(word)
    return result