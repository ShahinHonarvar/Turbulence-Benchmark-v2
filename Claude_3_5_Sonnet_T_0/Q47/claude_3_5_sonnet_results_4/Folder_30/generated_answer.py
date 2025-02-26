def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[14:91]
    for i in range(len(substring)):
        for j in range(i + 55, min(i + 72, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 55 and len(potential_palindrome) <= 71:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result