def palindromes_of_specific_lengths(s):
    palindromes = set()
    segment = s[33:86]
    segment = ''.join(filter(str.isalpha, segment)).lower()
    for start in range(len(segment)):
        for end in range(start + 26, min(start + 32, len(segment) + 1)):
            substring = segment[start:end]
            if len(substring) >= 26 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes