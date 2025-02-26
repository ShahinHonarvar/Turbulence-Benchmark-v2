def palindromes_of_specific_lengths(s):
    substring = s[12:93]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 42, min(i + 78, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 42 and len(potential_palindrome) <= 77:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result