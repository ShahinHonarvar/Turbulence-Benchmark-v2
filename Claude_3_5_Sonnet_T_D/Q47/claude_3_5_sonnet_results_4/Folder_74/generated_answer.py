def palindromes_of_specific_lengths(s):
    substring = s[30:85]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 21, len(substring) + 1)):
            if j - i > 20:
                break
            subseq = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if subseq == subseq[::-1] and 12 <= len(subseq) <= 20:
                result.add(subseq)
    return result