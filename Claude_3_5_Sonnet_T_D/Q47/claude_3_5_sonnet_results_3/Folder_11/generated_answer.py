def palindromes_of_specific_lengths(s):
    substring = s[24:98]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 37, len(substring) + 1)):
            subseq = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if 10 <= len(subseq) <= 36 and subseq == subseq[::-1]:
                result.add(subseq)
    return result