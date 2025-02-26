def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:97]
    for i in range(len(substring)):
        for j in range(i + 45, min(i + 53, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 45 <= len(cleaned_palindrome) <= 52:
                result.add(cleaned_palindrome)
    return result