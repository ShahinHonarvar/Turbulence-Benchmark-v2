def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[12:57]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes