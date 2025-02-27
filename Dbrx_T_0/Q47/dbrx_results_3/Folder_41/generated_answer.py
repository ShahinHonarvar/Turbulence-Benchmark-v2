def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, i + 5):
            if j < len(s) and s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes