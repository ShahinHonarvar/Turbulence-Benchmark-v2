def palindromes_of_specific_lengths(s):
    substring = s[18:88]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 38, min(i + 61, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 38 <= len(cleaned_palindrome) <= 60:
                result.add(cleaned_palindrome)
    return result