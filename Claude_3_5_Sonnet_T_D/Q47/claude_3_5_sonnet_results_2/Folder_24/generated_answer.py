def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[12:93]
    for i in range(len(substring)):
        for j in range(i + 42, min(i + 78, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if 42 <= len(cleaned_palindrome) <= 77 and cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1]:
                result.add(cleaned_palindrome)
    return result