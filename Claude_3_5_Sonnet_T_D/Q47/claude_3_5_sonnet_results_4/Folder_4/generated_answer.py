def palindromes_of_specific_lengths(s):
    substring = s[12:93]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 67, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            cleaned_palindrome = ''.join((c for c in potential_palindrome if c.isalpha()))
            if 17 <= len(cleaned_palindrome) <= 66 and cleaned_palindrome.lower() == cleaned_palindrome.lower()[::-1]:
                palindromes.add(cleaned_palindrome)
    return palindromes