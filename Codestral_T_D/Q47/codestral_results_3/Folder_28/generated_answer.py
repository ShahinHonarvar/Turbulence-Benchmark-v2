def palindromes_of_specific_lengths(s):
    if len(s) < 71:
        return set()
    substring = s[32:72]
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes