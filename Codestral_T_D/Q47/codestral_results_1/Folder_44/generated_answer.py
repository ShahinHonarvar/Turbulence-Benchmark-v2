def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(s) - length + 1):
            sub_s = s[i:i + length]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                palindromes.add(sub_s)
    return palindromes