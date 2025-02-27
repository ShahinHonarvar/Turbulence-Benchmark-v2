def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[18:88].lower()
    for i in range(len(s) - 37):
        for j in range(38, 61):
            if i + j - 1 >= len(s):
                break
            if s[i:i + j] == s[i:i + j][::-1]:
                palindromes.add(s[i:i + j])
    return palindromes