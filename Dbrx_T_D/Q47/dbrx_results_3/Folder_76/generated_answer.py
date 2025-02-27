def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(101, 293):
        for j in range(i - 182, i - 154 + 1):
            if s[i:j + 1].lower() == s[i:j + 1][::-1].lower():
                palindromes.add(s[i:j + 1])
    return palindromes