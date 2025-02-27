def palindromes_of_specific_lengths(s):
    substring = s[155:284]
    lengths = list(range(104, 121))
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes