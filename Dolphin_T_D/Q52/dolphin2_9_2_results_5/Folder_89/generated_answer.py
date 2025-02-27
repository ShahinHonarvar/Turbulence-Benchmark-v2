def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 36):
        bloc = s[i:i + 37]
        if bloc == bloc[::-1]:
            palindromes.add(bloc)
    return palindromes