def palindromes_of_specific_lengths(string):
    substring = string[34:91]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 14, i + 40):
            if j >= len(substring):
                break
            sub = substring[i:j + 1]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub.lower())
    return palindromes