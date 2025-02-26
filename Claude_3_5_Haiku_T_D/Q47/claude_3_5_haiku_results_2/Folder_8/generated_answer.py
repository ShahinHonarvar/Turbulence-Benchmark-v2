def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    palindromes = set()
    substring = s[17:73].lower()
    for start in range(len(substring)):
        for length in range(50, 52):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes