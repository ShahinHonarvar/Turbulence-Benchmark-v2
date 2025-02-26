def palindromes_of_specific_lengths(s):
    substring = s[23:83]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 32, min(i + 35, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome.lower() if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 32 <= len(cleaned_palindrome) <= 34:
                result.add(cleaned_palindrome)
    return result