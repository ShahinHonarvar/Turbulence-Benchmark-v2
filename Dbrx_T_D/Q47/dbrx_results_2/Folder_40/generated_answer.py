def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(0, 6):
        for j in range(i, i + 3):
            if j >= len(s):
                break
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes