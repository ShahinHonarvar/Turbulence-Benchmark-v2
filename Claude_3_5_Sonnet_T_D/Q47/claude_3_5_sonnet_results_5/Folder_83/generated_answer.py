def palindromes_of_specific_lengths(s):
    substring = s[75:96]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 7, min(i + 10, len(substring) + 1)):
            subseq = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if 7 <= len(subseq) <= 9 and subseq == subseq[::-1]:
                result.add(subseq)
    return result