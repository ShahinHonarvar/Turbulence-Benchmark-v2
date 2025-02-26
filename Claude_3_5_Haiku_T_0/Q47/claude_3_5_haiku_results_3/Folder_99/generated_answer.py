def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[127:289].lower()
    for length in range(119, 142):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes