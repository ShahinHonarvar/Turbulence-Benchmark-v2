def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(103, 276 + 1):
        for length in range(100, 169 + 1):
            sub_s = s[i:i + length].lower()
            if sub_s == sub_s[::-1] and all((c.isalpha() for c in sub_s)):
                palindromes.add(sub_s)
    return palindromes