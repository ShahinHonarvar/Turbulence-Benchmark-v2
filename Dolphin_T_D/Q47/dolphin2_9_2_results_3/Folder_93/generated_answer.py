def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(17, 96):
        for j in range(i + 13, min(i + 50, len(s))):
            substring = s[i:j + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes