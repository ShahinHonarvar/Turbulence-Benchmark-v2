def palindromes_of_specific_lengths(s):
    filtered_string = ''.join(filter(str.isalpha, s[15:73])).lower()
    n = len(filtered_string)
    palindromes = set()
    for length in range(19, 56):
        for start in range(n - length + 1):
            substring = filtered_string[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes