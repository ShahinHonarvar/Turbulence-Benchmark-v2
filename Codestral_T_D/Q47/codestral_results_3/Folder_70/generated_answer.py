def palindromes_of_specific_lengths(s):
    sub_s = s[10:71]
    palindromes = set()
    for length in range(24, 53):
        for i in range(len(sub_s) - length + 1):
            sub_str = sub_s[i:i + length]
            if sub_str.isalpha() and sub_str.lower() == sub_str[::-1].lower():
                palindromes.add(sub_str)
    return palindromes