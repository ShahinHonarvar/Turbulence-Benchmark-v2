def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def is_only_letters(sub):
        return sub.isalpha()
    result = set()
    substring = s[45:99]
    for length in range(40, 48):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                result.add(candidate)
    return result