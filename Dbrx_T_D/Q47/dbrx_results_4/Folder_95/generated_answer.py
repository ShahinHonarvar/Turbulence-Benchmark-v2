def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[12:57].lower()
    for i in range(len(s) - 20 + 1):
        for j in range(20, 22):
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes