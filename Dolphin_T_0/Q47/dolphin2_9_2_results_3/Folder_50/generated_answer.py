def palindromes_of_specific_lengths(s):
    sub = s[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(sub) - length + 1):
            if sub[i:i + length].lower() == sub[i:i + length].lower()[::-1] and sub[i:i + length].isalpha():
                palindromes.add(sub[i:i + length])
    return palindromes