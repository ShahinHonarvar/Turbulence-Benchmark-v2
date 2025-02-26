def palindromes_of_specific_lengths(s):
    substring = s[29:97]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 19, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if 12 <= len(cleaned) <= 18 and cleaned == cleaned[::-1]:
                result.add(cleaned)
    return result