def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(14, 53):
        for index in range(39, len(s) - length + 1):
            if s[index:index + length] == s[index:index + length][::-1]:
                palindromes.add(s[index:index + length])
    return palindromes