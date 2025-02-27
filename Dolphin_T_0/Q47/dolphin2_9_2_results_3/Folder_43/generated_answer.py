def palindromes_of_specific_lengths(s):
    substring = s[41:90]
    substring = ''.join((ch.lower() for ch in substring if ch.isalpha()))
    lengths = range(23, 39)
    palindromes = set()
    for length in lengths:
        for start_index in range(len(substring) - length + 1):
            if substring[start_index:start_index + length] == substring[start_index:start_index + length][::-1]:
                palindromes.add(substring[start_index:start_index + length])
    return palindromes