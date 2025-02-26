def palindromes_of_specific_lengths(s):
    s = s.lower()
    if len(s) <= 300:
        s = s[1:min(300, len(s))]
    else:
        s = s[1:300]
    palindromes = set()
    for length in range(3, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes