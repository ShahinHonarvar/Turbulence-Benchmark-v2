def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[32:80]
    for i in range(len(substring)):
        for j in range(i + 35, min(i + 42, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 35 <= len(potential_palindrome) <= 41:
                result.add(potential_palindrome)
    return result