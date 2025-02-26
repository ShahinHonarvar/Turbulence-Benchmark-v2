def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def is_letter_only(word):
        return word.isalpha()
    result = set()
    substring = s[127:289]
    for length in range(119, 142):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letter_only(candidate):
                result.add(candidate.lower())
    return result