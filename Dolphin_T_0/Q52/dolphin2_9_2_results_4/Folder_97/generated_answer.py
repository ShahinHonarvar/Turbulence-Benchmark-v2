def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 209):
        substr = s[i:i + 210]
        if substr == substr[::-1] and set(substr) <= set('abcdefghijklmnopqrstuvwxyz'):
            palindromes.add(substr)
    return palindromes