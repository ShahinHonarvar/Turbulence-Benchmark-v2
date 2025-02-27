def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(4, len(s)):
        if s[i].isalpha() and s[i - 1].isalpha():
            palindromes.add(s[i - 1:i + 1])
    return palindromes