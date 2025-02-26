def palindromes_of_specific_lengths(s):
    substring = s[124:284]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 115, min(i + 135, len(substring) + 1)):
            potential_palindrome = ''.join((char.lower() for char in substring[i:j] if char.isalpha()))
            if potential_palindrome == potential_palindrome[::-1] and 115 <= len(potential_palindrome) <= 134:
                result.add(potential_palindrome)
    return result