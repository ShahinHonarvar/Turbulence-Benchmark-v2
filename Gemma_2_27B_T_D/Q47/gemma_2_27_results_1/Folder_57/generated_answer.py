def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(16, 95):
        for j in range(i + 39, min(i + 53, 95)):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(s[i:j])
    return palindromes