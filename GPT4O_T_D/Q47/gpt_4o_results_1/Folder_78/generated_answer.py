from re import findall

def palindromes_of_specific_lengths(s):
    s = s[15:73]
    s = ''.join(findall('[a-zA-Z]', s)).lower()
    palindromes = set()
    for length in range(19, 56):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes