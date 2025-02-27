def palindromes_of_specific_lengths(s):
    filtered_s = ''.join((c.lower() for c in s[:101] if c.isalpha()))
    palindromes = set()
    for length in range(3, 16):
        for i in range(len(filtered_s) - length + 1):
            substr = filtered_s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes