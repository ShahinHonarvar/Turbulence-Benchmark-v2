def palindromes_of_specific_lengths(s):
    s = s[2:9]
    palindromes = set()
    for i in range(3, 5):
        for j in range(len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower():
                palindromes.add(s[j:j + i])
    return palindromes