def palindromes_of_specific_lengths(s):
    subset = s[11:84]
    result = set()
    for i in range(len(subset)):
        for j in range(i + 37, min(i + 61, len(subset) + 1)):
            substring = subset[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result