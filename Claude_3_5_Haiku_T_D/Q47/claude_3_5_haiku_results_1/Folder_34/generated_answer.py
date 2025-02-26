def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letters_only(word):
        return word.isalpha()
    result = set()
    if len(s) < 301:
        return result
    substring = s[200:301].lower()
    for length in range(10, 51):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letters_only(candidate):
                result.add(candidate)
    return result