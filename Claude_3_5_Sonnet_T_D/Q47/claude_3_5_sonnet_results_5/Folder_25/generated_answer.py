def palindromes_of_specific_lengths(string):
    substring = string[26:85]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 30, min(i + 47, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 30 <= len(potential_palindrome) <= 46:
                result.add(potential_palindrome)
    return result