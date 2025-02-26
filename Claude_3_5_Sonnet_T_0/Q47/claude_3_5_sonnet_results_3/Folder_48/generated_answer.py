def palindromes_of_specific_lengths(s):
    substring = s[155:284]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 104, min(i + 121, len(substring) + 1)):
            potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
            if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 104 <= len(potential_palindrome) <= 120:
                result.add(potential_palindrome)
    return result