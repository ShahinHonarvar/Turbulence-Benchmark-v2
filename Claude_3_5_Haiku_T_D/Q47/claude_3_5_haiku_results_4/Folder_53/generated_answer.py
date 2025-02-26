def palindromes_of_specific_lengths(s):
    substring = s[1:300].lower()
    palindromes = set()
    for length in range(3, 11):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes