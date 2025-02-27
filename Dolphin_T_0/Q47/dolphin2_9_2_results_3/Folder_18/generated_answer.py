def palindromes_of_specific_lengths(s):
    substring = s[11:84]
    lengths = set()
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1] and substring[i:i + length].isalpha():
                lengths.add(substring[i:i + length])
    return lengths