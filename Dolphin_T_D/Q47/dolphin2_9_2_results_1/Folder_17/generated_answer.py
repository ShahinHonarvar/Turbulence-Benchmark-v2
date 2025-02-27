def palindromes_of_specific_lengths(s):
    s = s[21:95]
    lengths = set()
    for length in range(52, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                lengths.add(substring)
    return lengths