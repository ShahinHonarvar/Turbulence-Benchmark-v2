def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[119:257]
    for i in range(len(substring)):
        for j in range(i + 104, min(i + 124, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if cleaned == cleaned[::-1] and 104 <= len(cleaned) <= 123:
                result.add(cleaned)
    return result