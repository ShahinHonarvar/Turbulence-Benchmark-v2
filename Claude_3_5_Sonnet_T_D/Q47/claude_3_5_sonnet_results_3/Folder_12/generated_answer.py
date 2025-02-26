def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 22, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 18 <= len(potential_palindrome) <= 21:
                result.add(potential_palindrome)
    return result