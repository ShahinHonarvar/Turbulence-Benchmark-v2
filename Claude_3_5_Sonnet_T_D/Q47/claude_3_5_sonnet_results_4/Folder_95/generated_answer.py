def palindromes_of_specific_lengths(s):
    substring = s[12:57]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 20, i + 22):
            if j <= len(substring):
                potential_palindrome = ''.join((c for c in substring[i:j] if c.isalpha()))
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1] and 20 <= len(potential_palindrome) <= 21:
                    result.add(potential_palindrome)
    return result