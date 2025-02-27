def palindromes_between_indices(s):
    start = 0
    end = 4
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes