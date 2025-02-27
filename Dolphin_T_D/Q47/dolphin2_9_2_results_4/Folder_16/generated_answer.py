def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(51, 61):
        for j in range(15, 87):
            if s[j:j + i].lower() == s[j:j + i].lower()[::-1] and all((c in string.ascii_lowercase for c in s[j:j + i].lower())):
                palindromes.add(s[j:j + i])
    return palindromes