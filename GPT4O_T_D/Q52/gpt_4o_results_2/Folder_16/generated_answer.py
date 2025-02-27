def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    if length < 255:
        return palindromes
    for i in range(length - 254):
        substr = s[i:i + 255]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes