def palindromes_of_specific_lengths(s):
    sub = s[17:87]
    results = set()
    for length in range(38, 61):
        for i in range(len(sub) - length + 1):
            if sub[i:i + length].lower() == sub[i:i + length].lower()[::-1]:
                results.add(sub[i:i + length].lower())
    return results