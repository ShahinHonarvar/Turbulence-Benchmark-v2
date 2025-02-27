def palindromes_of_specific_lengths(s):
    s = s[100:296]
    s = ''.join(filter(str.isalpha, s))
    palindromes_set = set()
    for length in range(136, 161):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes_set.add(substring)
    return palindromes_set