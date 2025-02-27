def palindromes_of_specific_lengths(s):
    substring = s[19:75]
    palindromes_set = set()
    for i in range(len(substring)):
        for j in range(i + 35, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1] and 36 <= len(sub) <= 42:
                palindrome = ''.join((c for c in sub if c.isalpha()))
                palindromes_set.add(palindrome.lower())
    return palindromes_set