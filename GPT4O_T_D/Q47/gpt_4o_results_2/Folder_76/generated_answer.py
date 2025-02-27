def palindromes_of_specific_lengths(s):
    substring = s[101:293]
    cleaned_substring = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for start in range(len(cleaned_substring)):
        for length in range(154, 183):
            end = start + length
            if end > len(cleaned_substring):
                break
            candidate = cleaned_substring[start:end]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes