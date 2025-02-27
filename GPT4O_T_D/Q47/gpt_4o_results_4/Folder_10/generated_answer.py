def palindromes_of_specific_lengths(s):
    s = s[16:61]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(16, 40):
            if i + j <= length:
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes