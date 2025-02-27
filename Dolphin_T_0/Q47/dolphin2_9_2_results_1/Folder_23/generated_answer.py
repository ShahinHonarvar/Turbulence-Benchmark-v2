def palindromes_of_specific_lengths(s):
    subS = s[22:95].lower()
    engAlphabets = set('abcdefghijklmnopqrstuvwxyz')
    subPalindromes = set()
    for len_pal in range(17, 56):
        for i in range(len(subS) - len_pal + 1):
            subStr = subS[i:i + len_pal]
            if set(subStr).issubset(engAlphabets) and subStr == subStr[::-1]:
                subPalindromes.add(subStr)
    return subPalindromes