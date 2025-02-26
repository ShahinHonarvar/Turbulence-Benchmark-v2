def palindromes_of_specific_lengths(s):
    if len(s) < 56:
        return set()
    substring = s[10:56].lower()
    palindromes = set()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes