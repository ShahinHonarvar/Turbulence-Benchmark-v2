def palindromes_of_specific_lengths(s):
    s = s[127:289]
    palindromes = set()
    for length in range(119, 142):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            filtered_substr = ''.join(filter(str.isalpha, substr)).lower()
            if filtered_substr == filtered_substr[::-1]:
                palindromes.add(substr)
    return palindromes