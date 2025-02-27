def palindromes_of_specific_lengths(s):
    s = s[100:201]
    palindromes = set()
    for i in range(5, 11):
        for j in range(len(s) - i + 1):
            stride = s[j:j + i]
            if stride == stride[::-1] and all((c.isalpha() for c in stride)):
                palindromes.add(stride.lower())
    return palindromes