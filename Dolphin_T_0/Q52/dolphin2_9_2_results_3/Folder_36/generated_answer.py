def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 337):
        substr = s[i:i + 338]
        if substr == substr[::-1]:
            if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substr)):
                palindromes.add(substr)
    return palindromes