def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        if s[i:i + 4] == s[i:i + 4][::-1] and s[i:i + 4].isalpha():
            palindromes.add(s[i:i + 4])
        if len(s) >= i + 5 and s[i:i + 5] == s[i:i + 5][::-1] and s[i:i + 5].isalpha():
            palindromes.add(s[i:i + 5])
    return palindromes