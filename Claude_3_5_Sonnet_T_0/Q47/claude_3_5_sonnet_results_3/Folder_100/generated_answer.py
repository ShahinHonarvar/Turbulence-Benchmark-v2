def palindromes_of_specific_lengths(s):
    substring = s[29:97]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 19, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if 12 <= len(cleaned_palindrome) <= 18 and cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1]:
                result.add(cleaned_palindrome)
    return result