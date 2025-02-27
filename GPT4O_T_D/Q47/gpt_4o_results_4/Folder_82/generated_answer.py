def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    start = max(3, 0)
    end = min(300, len(s) - 1)
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i + 30, min(end + 1, i + 301)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes