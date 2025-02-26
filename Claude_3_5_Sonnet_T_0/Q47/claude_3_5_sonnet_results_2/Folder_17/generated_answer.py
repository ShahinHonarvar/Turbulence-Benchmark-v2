def palindromes_of_specific_lengths(s):
    substring = s[22:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 52, min(i + 56, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if 52 <= len(cleaned_palindrome) <= 55 and cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1]:
                result.add(cleaned_palindrome)
    return result