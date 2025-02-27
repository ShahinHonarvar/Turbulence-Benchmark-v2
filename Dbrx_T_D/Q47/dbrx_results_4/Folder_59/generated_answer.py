def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(101):
        for j in range(3, 16):
            if i + j - 1 >= len(s):
                break
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes