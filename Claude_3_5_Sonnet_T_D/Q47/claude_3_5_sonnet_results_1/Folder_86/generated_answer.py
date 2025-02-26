def palindromes_of_specific_lengths(string):
    substring = string[30:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 34, min(i + 56, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 34 <= len(potential_palindrome) <= 55:
                result.add(potential_palindrome)
    return result