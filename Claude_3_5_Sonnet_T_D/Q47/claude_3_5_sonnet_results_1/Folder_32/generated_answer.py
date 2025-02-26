def palindromes_of_specific_lengths(s):
    substring = s[16:78]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 43, min(i + 48, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome.lower() if c.isalpha()))
            if cleaned_palindrome == cleaned_palindrome[::-1] and 43 <= len(cleaned_palindrome) <= 47:
                palindromes.add(potential_palindrome)
    return palindromes