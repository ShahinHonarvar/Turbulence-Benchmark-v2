def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[12:57].lower()
    for start in range(len(substring)):
        for end in range(start + 19, start + 22):
            if end > len(substring):
                break
            candidate = substring[start:end]
            if len(candidate) in (20, 21) and candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes