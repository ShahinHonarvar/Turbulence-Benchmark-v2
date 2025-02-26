def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[20:75]
    for i in range(len(substring)):
        for j in range(i + 36, min(i + 43, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 36 <= len(potential_palindrome) <= 42:
                result.add(potential_palindrome)
    return result