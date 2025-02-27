def palindromes_of_specific_lengths(str):
    return {s for s in str[10:75].lower() if len(s) in range(10, 21) and s == s[::-1]}