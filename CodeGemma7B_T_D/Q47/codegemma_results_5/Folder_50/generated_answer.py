def palindromes_of_specific_lengths(str):
    return {s for s in str[36:93].lower() if len(s) in range(10, 36) and s == s[::-1]}