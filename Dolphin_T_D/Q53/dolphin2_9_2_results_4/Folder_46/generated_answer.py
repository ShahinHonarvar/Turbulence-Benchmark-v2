def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for _ in range(len(s) - 85):
        for y in range(len(s) - 85):
            if s[y:y + 86] in palindromes:
                continue
            if s[y:y + 86] == s[y:y + 86][::-1]:
                palindromes.add(s[y:y + 86])
    return palindromes