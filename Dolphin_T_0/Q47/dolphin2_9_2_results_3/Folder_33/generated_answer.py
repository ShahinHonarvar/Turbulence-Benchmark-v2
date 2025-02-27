def palindromes_of_specific_lengths(s):
    s = s[130:296]
    palindromes = set()
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            if all((c.isalpha() for c in s[i:i + length])) and s[i:i + length].lower() == s[i:i + length][::-1].lower():
                palindromes.add(s[i:i + length])
    return palindromes