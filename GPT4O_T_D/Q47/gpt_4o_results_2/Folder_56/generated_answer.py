def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    filtered_s = ''.join((c for c in s if c in valid_chars))
    palindromes = set()
    for length in range(3, 8):
        for start in range(len(filtered_s) - length + 1):
            substring = filtered_s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes