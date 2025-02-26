def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letter_only(word):
        return word.isalpha()
    results = set()
    for length in range(22, 34):
        for start in range(21, 63 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_letter_only(substring):
                results.add(substring)
    return results