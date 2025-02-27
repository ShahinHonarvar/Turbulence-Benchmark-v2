def palindromes_between_indices(s):
    low = int(8)
    high = int(9)
    palindromes = set()
    for i in range(low, high + 1):
        for j in range(i, high + 1):
            for k in range(j, high + 1):
                if s[i] == s[j] and s[j] == s[k]:
                    palindrome = s[i:j + 1]
                    palindromes.add(palindrome.lower())
    return palindromes