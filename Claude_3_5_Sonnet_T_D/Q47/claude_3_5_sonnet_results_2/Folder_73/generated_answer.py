def palindromes_of_specific_lengths(s):
    substring = s[21:63]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 22, min(i + 34, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 22 <= len(potential_palindrome) <= 33:
                result.add(potential_palindrome)
    return result