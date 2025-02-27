def palindromes_of_specific_lengths(s):
    substring = s[13:100].lower()
    palindromes = set()
    for length in range(26, 30):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes