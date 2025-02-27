def palindromes_of_specific_lengths(s):
    s = s[26:88]
    palindromes = set()
    for i in range(52, 57):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes