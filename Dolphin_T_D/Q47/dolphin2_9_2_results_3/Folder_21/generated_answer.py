def palindromes_of_specific_lengths(s):
    s = s[100:296]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(136, 161):
        for i in range(length, len(s) + 1):
            if s[i - length:i] == s[i - length:i][::-1]:
                palindromes.add(s[i - length:i])
    return palindromes