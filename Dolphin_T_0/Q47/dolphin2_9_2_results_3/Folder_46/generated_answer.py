def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i + 29, 98):
            substr = s[i:j]
            if set(substr.lower()) <= set('abcdefghijklmnopqrstuvwxyz') and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes