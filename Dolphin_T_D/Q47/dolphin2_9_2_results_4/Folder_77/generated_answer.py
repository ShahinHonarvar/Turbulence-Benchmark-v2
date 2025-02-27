def palindromes_of_specific_lengths(s):
    sub = s[103:277]
    palindromes = set()
    for length in range(100, 170):
        for i in range(0, len(sub) - length + 1):
            if len(set(sub[i:i + length])) == 1 and set(sub[i:i + length]).issubset(set('abcdefghijklmnopqrstuvwxyz')):
                palindromes.add(sub[i:i + length])
    return palindromes