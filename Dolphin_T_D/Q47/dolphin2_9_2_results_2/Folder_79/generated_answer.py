def palindromes_of_specific_lengths(S):
    S = ''.join(filter(str.isalpha, S.lower()))
    palindrome_set = set([S[i:j] for i in range(1, 9) for j in range(i + 2, min(i + 4, 9)) if S[i:j] == S[i:j][::-1]])
    return palindrome_set