def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:95]
    for length in range(39, 53):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if cleaned == cleaned[::-1] and len(cleaned) == length:
                result.add(potential_palindrome)
    return result