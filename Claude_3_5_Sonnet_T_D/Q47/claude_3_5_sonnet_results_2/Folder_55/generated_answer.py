def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:76]

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 21, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result