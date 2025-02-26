def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:71]
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 53, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned == cleaned[::-1] and 24 <= len(cleaned) <= 52:
                result.add(cleaned)
    return result