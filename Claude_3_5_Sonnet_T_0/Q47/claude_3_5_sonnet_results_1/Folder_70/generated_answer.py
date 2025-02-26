def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:71]
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 53, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 24 and len(potential_palindrome) <= 52:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result