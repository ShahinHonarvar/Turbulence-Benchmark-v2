def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[17:96]
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 50, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned = ''.join(filter(str.isalpha, potential_palindrome)).lower()
            if cleaned == cleaned[::-1] and 13 <= len(cleaned) <= 49:
                result.add(cleaned)
    return result