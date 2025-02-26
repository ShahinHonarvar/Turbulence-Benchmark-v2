def palindromes_of_specific_lengths(s):
    substring = s[75:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 7, min(i + 10, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 7 <= len(potential_palindrome) <= 9:
                result.add(potential_palindrome)
    return result