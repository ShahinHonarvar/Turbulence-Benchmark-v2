def palindrome_of_length_n(S):
    S = S.lower()
    palindromes_set = set()
    for i in range(len(S)):
        if i + 74 <= len(S):
            sub_str = S[i:i + 74]
            reversed_sub_str = sub_str[::-1]
            if sub_str == reversed_sub_str:
                if set('abcdefghijklmnopqrstuvwxyz').issubset(set(sub_str)):
                    palindromes_set.add(sub_str)
    return palindromes_set