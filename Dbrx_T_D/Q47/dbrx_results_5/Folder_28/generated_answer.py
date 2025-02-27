def palindromes_of_specific_lengths(s):
    palindromes = set()
    target_len = range(21, 33)
    for i in target_len:
        for j in range(32, len(s) - i + 1):
            candidate = s[j:j + i].lower()
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes