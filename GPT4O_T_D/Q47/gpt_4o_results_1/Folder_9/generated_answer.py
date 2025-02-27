def palindromes_of_specific_lengths(s):
    s = s[:301]
    filtered_string = ''.join((c.lower() for c in s if c.isalpha()))
    valid_lengths = range(50, 61)
    palindromes = set()
    for start in range(len(filtered_string)):
        for length in valid_lengths:
            end = start + length
            if end <= len(filtered_string):
                substring = filtered_string[start:end]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes