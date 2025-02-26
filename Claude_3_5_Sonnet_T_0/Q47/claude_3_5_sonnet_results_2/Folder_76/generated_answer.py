def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 154, min(i + 183, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome.lower() if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 154 <= len(cleaned_palindrome) <= 182:
                result.add(potential_palindrome)
    return result