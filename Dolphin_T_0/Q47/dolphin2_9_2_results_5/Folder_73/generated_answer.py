def palindromes_of_specific_lengths(s):
    s = s[21:63]
    palindromes = set()
    for i in range(22, 34):
        for j in range(0, len(s) - i + 1):
            subS = s[j:j + i]
            if subS == subS[::-1] and subS.isalpha():
                palindromes.add(subS.lower())
    return palindromes