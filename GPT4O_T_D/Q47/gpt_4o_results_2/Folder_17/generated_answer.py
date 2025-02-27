def palindromes_of_specific_lengths(s):
    start, end = (22, 95)
    min_len, max_len = (52, 55)
    substring = ''.join(filter(str.isalpha, s[start:end + 1])).lower()
    palindromes = set()
    for length in range(min_len, max_len + 1):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if part == part[::-1]:
                palindromes.add(part)
    return palindromes