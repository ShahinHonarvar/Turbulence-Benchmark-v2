def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    substring = s[:8].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 6, len(substring) + 1)):
            candidate = substring[i:j]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes