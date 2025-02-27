def palindromes_of_specific_lengths(s):
    sub_s = s[10:56]
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(sub_s) - length + 1):
            substring = sub_s[i:i + length]
            substring = substring.lower()
            if len(set(substring)) == len(substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes