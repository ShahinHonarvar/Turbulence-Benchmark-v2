def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    palindromes = set()
    substring = s[17:73]
    for start in range(len(substring)):
        for length in range(50, 52):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate) and is_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes