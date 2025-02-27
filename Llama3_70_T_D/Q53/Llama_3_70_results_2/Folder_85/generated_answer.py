def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(85, len(s) + 1):
        for i in range(len(s) - length + 1):
            subs = ''.join(filter(str.isalpha, s[i:i + length]))
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes