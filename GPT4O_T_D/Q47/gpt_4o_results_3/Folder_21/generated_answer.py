def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    alpha_only = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(136, 161):
        if length <= len(alpha_only):
            for start in range(len(alpha_only) - length + 1):
                substr = alpha_only[start:start + length]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes