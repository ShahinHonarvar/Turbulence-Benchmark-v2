def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:56]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 8, len(substring) + 1)):
            word = substring[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                result.add(word.lower())
    return result