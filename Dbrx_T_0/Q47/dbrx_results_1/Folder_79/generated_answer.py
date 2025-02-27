def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(1, 9):
        for j in range(len(s) - i + 1):
            if i >= 3 and i <= 4 and (s[j:j + i] == s[j:j + i][::-1]) and s[j:j + i].isalpha():
                palindromes.add(s[j:j + i])
    return palindromes