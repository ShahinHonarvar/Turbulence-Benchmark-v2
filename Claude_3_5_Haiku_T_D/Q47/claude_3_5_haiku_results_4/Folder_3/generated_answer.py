def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 96:
        return palindromes
    substring = s[27:96]
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            candidate = substring[i:j + 1]
            if 49 <= len(candidate) <= 51 and candidate.isalpha():
                lowercase_candidate = candidate.lower()
                if lowercase_candidate == lowercase_candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes