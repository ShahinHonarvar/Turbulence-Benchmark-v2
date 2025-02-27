def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    target_length = 59
    for i in range(len(s) - target_length + 1):
        substr = s[i:i + target_length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes