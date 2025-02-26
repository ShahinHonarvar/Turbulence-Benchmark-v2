def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:84]
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 67, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 13 <= len(potential_palindrome) <= 66:
                result.add(potential_palindrome)
    return result