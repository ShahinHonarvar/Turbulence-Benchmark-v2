def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 12):
        substr = s[i:i + 13]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes