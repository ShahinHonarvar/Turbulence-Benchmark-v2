def palindromes_of_specific_lengths(s):
    sub_s = s[22:96]
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(sub_s) - length + 1):
            subs_c = sub_s[i:i + length]
            if subs_c == subs_c[::-1] and subs_c.isalpha():
                palindromes.add(subs_c.lower())
    return palindromes