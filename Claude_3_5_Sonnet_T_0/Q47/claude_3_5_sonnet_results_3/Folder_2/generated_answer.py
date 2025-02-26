def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:60]
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 37, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 18 and len(potential_palindrome) <= 36:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result