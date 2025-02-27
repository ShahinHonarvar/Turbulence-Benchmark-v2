def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[:7])).lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes