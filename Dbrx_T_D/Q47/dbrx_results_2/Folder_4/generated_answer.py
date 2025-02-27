def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    palindromes = set()
    for length in range(17, 67):
        for index in range(len(s) - length + 1):
            if s[index:index + length] == s[index:index + length][::-1]:
                palindromes.add(s[index:index + length])
    return palindromes