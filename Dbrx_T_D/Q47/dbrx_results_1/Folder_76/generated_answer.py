def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(101, 293):
        for j in range(i - 154, i - 181):
            if s[i] < 'a' or s[i] > 'z':
                continue
            substring = s[j:i + 1].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes