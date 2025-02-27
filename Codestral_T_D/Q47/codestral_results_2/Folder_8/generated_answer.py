def palindromes_of_specific_lengths(s):
    s = s[17:73]
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(s) - length + 1):
            sub_str = s[i:i + length]
            if sub_str.lower() == sub_str[::-1].lower() and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes