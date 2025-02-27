def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(27, 78):
        for j in range(i + 18, min(i + 20, 79)):
            substring = s[i:j]
            if len(substring) >= 18 and substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes