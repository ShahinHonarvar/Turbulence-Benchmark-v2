def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[65:100]
    for i in range(len(substring)):
        for j in range(i + 26, min(i + 34, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 26 <= len(potential_palindrome) <= 33:
                result.add(potential_palindrome)
    return result