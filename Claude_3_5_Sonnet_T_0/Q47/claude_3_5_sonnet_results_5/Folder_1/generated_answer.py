def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:90]
    for i in range(len(substring)):
        for j in range(i + 40, min(i + 73, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if len(potential_palindrome) >= 40 and len(potential_palindrome) <= 72:
                if potential_palindrome == potential_palindrome[::-1]:
                    result.add(potential_palindrome)
    return result