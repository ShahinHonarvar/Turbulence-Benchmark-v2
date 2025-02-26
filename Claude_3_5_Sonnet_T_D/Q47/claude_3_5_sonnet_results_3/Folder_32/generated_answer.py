def palindromes_of_specific_lengths(s):
    substring = s[16:78]
    result = set()
    for i in range(len(substring)):
        for length in range(43, 48):
            if i + length <= len(substring):
                potential_palindrome = substring[i:i + length]
                cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
                if cleaned == cleaned[::-1] and len(cleaned) == length:
                    result.add(potential_palindrome)
    return result