def palindromes_of_specific_lengths(st):
    st = st[22:96]
    palindromes = set()
    for length in range(52, 56):
        for i in range(len(st) - length + 1):
            substring = st[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes