def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[31:75]
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 40, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 23 and len(potential_palindrome) <= 39 and (potential_palindrome == potential_palindrome[::-1]):
                result.add(potential_palindrome)
    return result