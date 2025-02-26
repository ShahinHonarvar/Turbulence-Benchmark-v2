def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[1:9]
    for i in range(len(substr)):
        for j in range(i + 3, min(i + 5, len(substr) + 1)):
            word = substr[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                result.add(word.lower())
    return result