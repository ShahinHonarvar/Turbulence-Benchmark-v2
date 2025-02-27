def palindromes_of_specific_lengths(s):
    s = s[45:99]
    lengths = range(40, 48)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes