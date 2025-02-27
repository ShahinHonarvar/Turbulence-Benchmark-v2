def palindromes_of_specific_lengths(s):
    substring = s[29:97]
    results = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                results.add(sub)
    return results