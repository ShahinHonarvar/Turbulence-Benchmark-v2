def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[28:95]
    for i in range(len(substring)):
        for j in range(i + 38, min(i + 50, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 38 <= len(cleaned_palindrome) <= 49:
                result.add(cleaned_palindrome)
    return result