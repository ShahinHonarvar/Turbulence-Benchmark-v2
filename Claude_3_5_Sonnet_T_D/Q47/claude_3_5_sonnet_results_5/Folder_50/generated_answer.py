def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[36:93]
    for i in range(len(substr)):
        for j in range(i + 10, min(i + 36, len(substr) + 1)):
            potential_palindrome = ''.join((c.lower() for c in substr[i:j] if c.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 10 <= len(potential_palindrome) <= 35:
                result.add(potential_palindrome)
    return result