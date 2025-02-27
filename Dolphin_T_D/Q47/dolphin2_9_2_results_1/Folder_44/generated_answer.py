def palindromes_of_specific_lengths(s):
    s = s[17:98].lower()
    palindromes = set()
    for length in range(31, 52):
        palindromes.update([s[i:i + length] for i in range(len(s) - length + 1) if s[i:i + length] == s[i:i + length][::-1] and s[i:i + length].isalpha()])
    return palindromes