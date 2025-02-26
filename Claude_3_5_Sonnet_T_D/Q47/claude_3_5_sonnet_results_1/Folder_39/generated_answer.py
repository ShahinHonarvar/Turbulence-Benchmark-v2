def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[31:92]
    for i in range(len(substring)):
        for length in range(50, 54):
            if i + length <= len(substring):
                potential_palindrome = ''.join((c for c in substring[i:i + length] if c.isalpha()))
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 50 <= len(potential_palindrome) <= 53:
                    result.add(potential_palindrome)
    return result