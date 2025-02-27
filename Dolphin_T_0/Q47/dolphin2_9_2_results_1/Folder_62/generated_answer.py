def palindromes_of_specific_lengths(s):
    sub = s[26:88]
    palindromes = set()
    for i in range(52, 57):
        for j in range(0, len(sub) - i + 1):
            if sub[j:j + i].lower() == sub[j:j + i].lower()[::-1] and sub[j:j + i].isalpha():
                palindromes.add(sub[j:j + i])
    return palindromes