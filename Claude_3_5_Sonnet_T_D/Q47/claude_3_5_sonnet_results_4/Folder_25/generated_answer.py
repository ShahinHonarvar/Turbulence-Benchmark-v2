def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[26:85]
    for i in range(len(substr)):
        for j in range(i + 30, min(i + 47, len(substr) + 1)):
            potential_palindrome = substr[i:j]
            cleaned = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if cleaned == cleaned[::-1] and 30 <= len(cleaned) <= 46:
                result.add(cleaned)
    return result