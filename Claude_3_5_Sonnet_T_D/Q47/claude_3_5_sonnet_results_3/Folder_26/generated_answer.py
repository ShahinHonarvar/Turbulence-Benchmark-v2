def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[24:85]
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 32, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1] and 21 <= len(cleaned_palindrome) <= 31:
                result.add(cleaned_palindrome)
    return result