def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(0, 7):
        for j in range(i + 2, 7):
            sub = s[i:j + 1]
            for length in range(3, 7):
                for k in range(0, j - i + 1 - length + 1):
                    chrom = sub[k:k + length]
                    if len(chrom) == len(set(chrom.lower())) and chrom.lower() == chrom[::-1].lower():
                        result.add(chrom)
    return result