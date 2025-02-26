def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[11:98]
    for i in range(len(substr)):
        for j in range(i + 29, min(i + 63, len(substr) + 1)):
            word = substr[i:j]
            if word.isalpha() and word.lower() == word.lower()[::-1]:
                result.add(word)
    return result