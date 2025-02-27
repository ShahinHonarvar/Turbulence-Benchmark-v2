def palindromes_of_specific_lengths(s):
    s = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(s) - length + 1):
            sub_s = s[i:i + length]
            if sub_s.lower() == sub_s[::-1].lower() and sub_s.isalpha():
                palindromes.add(sub_s)
    return palindromes