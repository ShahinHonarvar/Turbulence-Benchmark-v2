def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[34:91]
    filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
    n = len(filtered_substring)
    for length in range(14, 40):
        for start in range(n - length + 1):
            candidate = filtered_substring[start:start + length]
            if candidate == candidate[::-1]:
                palindromes.add(substring[start:start + length])
    return palindromes