def palindromes_of_specific_lengths(s):
    if not 26 <= 90 < len(s):
        return set()
    substring = s[26:91]
    palindromes = set()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes