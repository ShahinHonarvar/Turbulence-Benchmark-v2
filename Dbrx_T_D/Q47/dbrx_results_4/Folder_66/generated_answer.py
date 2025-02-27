def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(35, 42):
        for index in range(32, len(s) - length + 1):
            if s[index:index + length] == s[index:index + length][::-1]:
                palindromes.add(s[index:index + length])
    return palindromes