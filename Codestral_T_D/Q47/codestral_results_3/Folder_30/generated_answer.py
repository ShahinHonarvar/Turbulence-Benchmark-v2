def palindromes_of_specific_lengths(s):
    s = s[14:91]
    palindromes = set()
    for length in range(55, 72):
        for i in range(len(s) - length + 1):
            sub_s = s[i:i + length]
            if sub_s.isalpha() and sub_s.lower() == sub_s.lower()[::-1]:
                palindromes.add(sub_s)
    return palindromes