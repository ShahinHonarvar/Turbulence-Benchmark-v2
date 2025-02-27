def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(len(s) - 20 + 1):
        for j in range(i, min(i + 31, len(s) + 1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes