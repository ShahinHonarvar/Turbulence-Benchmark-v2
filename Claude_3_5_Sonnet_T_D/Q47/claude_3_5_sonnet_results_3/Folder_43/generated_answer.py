def palindromes_of_specific_lengths(s):
    substring = s[41:90]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 39, len(substring) + 1)):
            segment = substring[i:j]
            if segment.isalpha() and segment.lower() == segment.lower()[::-1]:
                palindromes.add(segment)
    return palindromes