def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:99]
    for i in range(len(substring)):
        for j in range(i + 31, min(i + 52, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            clean_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if clean_palindrome.lower() == clean_palindrome.lower()[::-1] and 31 <= len(clean_palindrome) <= 51:
                result.add(clean_palindrome)
    return result