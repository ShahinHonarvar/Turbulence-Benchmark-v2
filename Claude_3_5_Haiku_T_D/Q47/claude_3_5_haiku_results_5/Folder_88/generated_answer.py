def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[11:88].lower()
    for start in range(len(substring)):
        for length in range(4, 6):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if len(candidate) == 4 or len(candidate) == 5:
                if candidate == candidate[::-1] and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes