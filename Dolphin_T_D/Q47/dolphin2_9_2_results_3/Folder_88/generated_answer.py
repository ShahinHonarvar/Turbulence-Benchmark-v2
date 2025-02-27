def palindromes_of_specific_lengths(s):
    subset = s[11:88]
    lengths = [4, 5]
    palindromes = set()
    for length in lengths:
        for i in range(len(subset) - length + 1):
            candidate = subset[i:i + length]
            if candidate == candidate.lower() and candidate[::-1] == candidate.lower() and all((c in 'abcdefghijklmnopqrstuvwxyz' for c in candidate)):
                palindromes.add(candidate)
    return palindromes