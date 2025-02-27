def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[65:100]
    clean_substring = ''.join((c for c in substring if c.isalpha())).lower()
    length_range = range(26, 34)
    result = set()
    for length in length_range:
        for i in range(len(clean_substring) - length + 1):
            candidate = clean_substring[i:i + length]
            if is_palindrome(candidate):
                result.add(candidate)
    return result