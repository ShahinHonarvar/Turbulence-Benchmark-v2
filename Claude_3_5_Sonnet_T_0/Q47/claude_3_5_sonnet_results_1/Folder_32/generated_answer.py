def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:78]
    for i in range(len(substring)):
        for j in range(i + 43, min(i + 48, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned == cleaned[::-1] and 43 <= len(cleaned) <= 47:
                result.add(potential_palindrome)
    return result