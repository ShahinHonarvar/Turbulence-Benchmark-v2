def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[125:284]
    for i in range(len(substring)):
        for j in range(i + 109, min(i + 127, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c.lower() for c in potential_palindrome if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 109 <= len(cleaned_palindrome) <= 126:
                result.add(potential_palindrome)
    return result