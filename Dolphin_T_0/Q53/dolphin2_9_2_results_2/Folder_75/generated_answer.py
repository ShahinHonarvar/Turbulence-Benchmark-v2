def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 40):
        for j in range(i + 40, len(s) + 1):
            subset = s[i:j]
            if subset == subset[::-1]:
                palindromes.add(subset)
    return palindromes