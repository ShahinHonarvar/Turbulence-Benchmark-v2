def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 84):
        substr = s[i:i + 85]
        if substr == substr[::-1] and set(substr).issubset('abcdefghijklmnopqrstuvwxyz'):
            palindromes.add(substr)
    return palindromes