def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[:8]
    palindromes = set()
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length <= len(substring):
                candidate = substring[i:i + length]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate.lower())
    return palindromes