def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(87, len(s) + 1):
        for i in range(len(s) - length + 1):
            subs = s[i:i + length]
            if subs.isalpha() and subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes