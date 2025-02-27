def palindromes_of_specific_lengths(s):
    substr = s[10:56]
    palindromes = set()
    for length in range(3, 8):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            filtered_candidate = ''.join(filter(str.isalpha, candidate))
            if len(filtered_candidate) == length and filtered_candidate.lower() == filtered_candidate[::-1].lower():
                palindromes.add(filtered_candidate.lower())
    return palindromes