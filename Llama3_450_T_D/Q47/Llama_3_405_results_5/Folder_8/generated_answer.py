def palindromes_of_specific_lengths(s):
    s = s[17:73].lower()
    palindromes = set()
    for i in range(len(s) - 49):
        for j in range(i + 50, i + 52):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes