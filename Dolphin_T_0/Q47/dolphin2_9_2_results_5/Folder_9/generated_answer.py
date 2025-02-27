def palindromes_of_specific_lengths(s):
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    subs = s[:301]
    palindromes = set()
    for length in range(50, 61):
        for start in range(0, 301 - length):
            if subs[start:start + length] == subs[start:start + length][::-1]:
                palindromes.add(subs[start:start + length])
    return palindromes