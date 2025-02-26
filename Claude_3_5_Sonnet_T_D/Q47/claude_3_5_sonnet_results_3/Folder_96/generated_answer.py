def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:301]
    for i in range(len(substring)):
        for j in range(i + 50, min(i + 101, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if 50 <= len(cleaned) <= 100 and cleaned == cleaned[::-1]:
                result.add(cleaned)
    return result