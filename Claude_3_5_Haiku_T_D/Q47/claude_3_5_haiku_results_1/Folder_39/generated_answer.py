def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[31:92]
    for length in range(50, 54):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and len(candidate) == length:
                lower_candidate = candidate.lower()
                if lower_candidate == lower_candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes