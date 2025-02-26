def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def is_only_letters(s):
        return s.isalpha()
    substring = text[200:301].lower()
    result_set = set()
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                result_set.add(candidate)
    return result_set