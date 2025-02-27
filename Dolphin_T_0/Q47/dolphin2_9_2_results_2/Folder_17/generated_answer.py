def palindromes_of_specific_lengths(s):
    substring = s[22:96]
    lengths = set()
    for length in range(52, 56):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub.lower() and sub == sub[::-1].lower():
                lengths.add(sub)
    return lengths