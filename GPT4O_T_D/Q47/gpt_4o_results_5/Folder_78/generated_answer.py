def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    s = s[15:73]
    s = ''.join(filter(str.isalpha, s))
    low = 0
    high = len(s)
    s = s.lower()
    for length in range(19, 56):
        for i in range(high - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                valid_palindromes.add(substr)
    return valid_palindromes