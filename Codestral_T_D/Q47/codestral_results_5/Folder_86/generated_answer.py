def palindromes_of_specific_lengths(s):
    s = s[30:96]
    s = ''.join(filter(str.isalpha, s)).lower()
    output = set()
    for length in range(34, 56):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                output.add(substring)
    return output