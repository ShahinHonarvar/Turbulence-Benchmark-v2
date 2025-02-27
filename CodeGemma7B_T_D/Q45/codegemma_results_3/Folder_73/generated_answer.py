def palindromes_between_indices(s):
    range_start = 3
    range_end = 6
    palindromes = set()
    for i in range(range_start, range_end + 1):
        for j in range(i, range_end + 1):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    if not palindromes:
        palindromes = set()
    return palindromes