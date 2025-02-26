def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:89]
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 15, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if 12 <= len(cleaned) <= 14 and cleaned == cleaned[::-1]:
                result.add(potential_palindrome)
    return result