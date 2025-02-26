def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    substring = s[:8]
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            if j - i in (4, 5):
                candidate = substring[i:j]
                if candidate == candidate[::-1] and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes