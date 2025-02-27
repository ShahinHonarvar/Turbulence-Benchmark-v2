def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(27, 95 + 1):
        for length in range(49, 51 + 1):
            candidate = text[i:i + length]
            if candidate.lower() == candidate.lower()[::-1] and all((c in 'abcdefghijklmnopqrstuvwxyz' for c in candidate)):
                palindromes.add(candidate)
    return palindromes