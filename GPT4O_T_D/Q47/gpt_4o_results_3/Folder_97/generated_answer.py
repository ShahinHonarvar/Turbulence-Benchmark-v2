def palindromes_of_specific_lengths(s):
    s = s[28:95]
    filtered_string = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for start in range(len(filtered_string)):
        for length in range(38, 50):
            if start + length <= len(filtered_string):
                substring = filtered_string[start:start + length]
                if substring == substring[::-1]:
                    palindromes.add(s[start:start + length])
    return palindromes