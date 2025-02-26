def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[45:99]
    for i in range(len(substring)):
        for j in range(i + 40, min(i + 48, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join((char.lower() for char in potential_palindrome if char.isalpha()))
            if 40 <= len(cleaned) <= 47 and cleaned == cleaned[::-1]:
                result.add(cleaned)
    return result