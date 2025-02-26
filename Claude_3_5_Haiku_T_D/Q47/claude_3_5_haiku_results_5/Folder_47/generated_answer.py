def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def is_alpha_only(word):
        return word.isalpha()
    palindromes = set()
    substring = s[39:95]
    for length in range(14, 53):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_alpha_only(candidate):
                palindromes.add(candidate.lower())
    return palindromes