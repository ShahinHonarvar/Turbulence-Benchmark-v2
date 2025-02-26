def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 154, min(i + 183, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if 154 <= len(cleaned_palindrome) <= 182 and cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1]:
                result.add(cleaned_palindrome)
    return result