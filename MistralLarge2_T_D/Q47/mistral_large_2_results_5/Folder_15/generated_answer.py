def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    substring = s[:7].lower()
    for length in range(3, 7):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result