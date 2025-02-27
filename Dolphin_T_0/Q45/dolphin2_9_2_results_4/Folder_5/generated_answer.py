def palindromes_between_indices(s):
    letters = set(s[4:9].lower())
    result = set()
    for word in letters ** 2:
        if len(word) >= 4 and word == word[::-1]:
            result.add(word)
    return result