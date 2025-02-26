def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:296]
    for i in range(len(substring)):
        for j in range(i + 136, min(i + 161, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 136 <= len(potential_palindrome) <= 160:
                result.add(potential_palindrome)
    return result