def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[33:86]
    for i in range(len(substring)):
        for length in range(26, 32):
            if i + length <= len(substring):
                potential_palindrome = ''.join(filter(str.isalpha, substring[i:i + length])).lower()
                if potential_palindrome == potential_palindrome[::-1] and len(potential_palindrome) == length:
                    result.add(potential_palindrome)
    return result