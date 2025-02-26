def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:85]
    for i in range(len(substring)):
        for j in range(i + 30, min(i + 47, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome.lower() if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 30 <= len(cleaned_palindrome) <= 46:
                result.add(cleaned_palindrome)
    return result