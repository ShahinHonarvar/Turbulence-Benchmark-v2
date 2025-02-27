def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    palindromes = set()
    for i in range(52, 56):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                palindromes.add(s[j:j + i])
    return palindromes