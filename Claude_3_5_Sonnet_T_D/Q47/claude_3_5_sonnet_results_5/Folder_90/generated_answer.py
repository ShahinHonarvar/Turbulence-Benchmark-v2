def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[106:281]
    for start in range(len(substring)):
        for end in range(start + 136, min(start + 152, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[start:end])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 136 <= len(potential_palindrome) <= 151:
                result.add(potential_palindrome)
    return result