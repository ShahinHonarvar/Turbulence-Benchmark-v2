def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) > 50:
        s = s[0:50]
    for i in range(50, 101):
        for j in range(0, len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i].lower()[::-1]:
                palindromes.add(s[j:j + i])
    return palindromes