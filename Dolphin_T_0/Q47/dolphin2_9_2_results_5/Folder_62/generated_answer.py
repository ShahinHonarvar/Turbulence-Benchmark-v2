def palindromes_of_specific_lengths(s):
    s = s[25:87]
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes