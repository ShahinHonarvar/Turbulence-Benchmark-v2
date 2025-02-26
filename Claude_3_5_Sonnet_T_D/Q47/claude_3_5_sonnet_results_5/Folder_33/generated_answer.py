def palindromes_of_specific_lengths(s):
    substring = s[130:296]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 103, min(i + 159, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 103 <= len(potential_palindrome) <= 158:
                result.add(potential_palindrome)
    return result