def palindromes_of_specific_lengths(s):
    s = s[15:95]
    palindromes = set()
    for length in range(18, 74):
        for i in range(len(s) - length + 1):
            subster = s[i:i + length]
            if subster == subster[::-1] and subster.isalpha():
                palindromes.add(subster)
    return palindromes