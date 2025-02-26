def palindromes_of_specific_lengths(s):
    if len(s) < 301:
        return set()
    substring = s[100:301].lower()
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes