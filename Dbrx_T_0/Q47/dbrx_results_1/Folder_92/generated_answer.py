def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(5):
        for j in range(len(s) - i):
            if i + 3 < len(s) and s[j:j + i + 3] == s[j:j + i + 3][::-1] and s[j:j + i + 3].isalpha():
                palindromes.add(s[j:j + i + 3])
            if i + 4 < len(s) and s[j:j + i + 4] == s[j:j + i + 4][::-1] and s[j:j + i + 4].isalpha():
                palindromes.add(s[j:j + i + 4])
    return palindromes