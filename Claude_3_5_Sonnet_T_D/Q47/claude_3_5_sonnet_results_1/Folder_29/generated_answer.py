def palindromes_of_specific_lengths(s):
    substring = s[15:95]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 74, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if 18 <= len(cleaned) <= 73 and cleaned == cleaned[::-1]:
                result.add(cleaned)
    return result