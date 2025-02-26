def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 56, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if 17 <= len(cleaned_palindrome) <= 55 and cleaned_palindrome == cleaned_palindrome[::-1]:
                result.add(cleaned_palindrome)
    return result