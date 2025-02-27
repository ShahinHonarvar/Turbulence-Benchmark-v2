def palindrome_of_length_n(S):
    S = ''.join([c.lower() for c in S if c.isalpha()])
    n = 54
    palindromes = set()
    for i in range(len(S) - n + 1):
        subS = S[i:i + n]
        if subS == subS[::-1]:
            palindromes.add(subS)
    return palindromes