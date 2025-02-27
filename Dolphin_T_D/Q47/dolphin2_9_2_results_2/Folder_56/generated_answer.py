def palindromes_of_specific_lengths(s):
    s = s[1:10]
    palindromes = set()
    for length in range(3, 8):
        for start_idx in range(0, len(s) - length + 1):
            substring = s[start_idx:start_idx + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes