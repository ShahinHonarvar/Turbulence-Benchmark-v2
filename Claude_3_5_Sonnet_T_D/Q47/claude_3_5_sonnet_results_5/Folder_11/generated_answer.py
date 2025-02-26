def palindromes_of_specific_lengths(s):
    substring = s[24:98]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 37, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 10 <= len(potential_palindrome) <= 36:
                result.add(potential_palindrome)
    return result