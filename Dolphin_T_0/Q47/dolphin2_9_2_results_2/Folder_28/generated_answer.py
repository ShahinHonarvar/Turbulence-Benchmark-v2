def palindromes_of_specific_lengths(s):
    sub_s = s[31:72]
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(sub_s) - length + 1):
            sub_pal = sub_s[i:i + length].lower()
            if sub_pal == sub_pal[::-1] and sub_pal.isalpha():
                palindromes.add(sub_pal)
    return palindromes