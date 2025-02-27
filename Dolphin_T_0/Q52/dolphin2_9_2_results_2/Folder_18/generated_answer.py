def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 391):
        if s[i:i + 392] == s[i:i + 392][::-1]:
            palindromes.add(s[i:i + 392])
    return palindromes