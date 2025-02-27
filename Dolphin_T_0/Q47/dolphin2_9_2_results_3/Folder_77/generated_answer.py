def palindromes_of_specific_lengths(s):
    s = s[102:277]
    palindromes = set()
    for i in range(100, 170):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes