def palindrome_of_length_n(s):
    palindromes = set()
    n = 6
    for i in range(len(s) - n + 1):
        if s[i:i + n].lower() == s[i:i + n][::-1].lower():
            palindromes.add(s[i:i + n])
    return palindromes