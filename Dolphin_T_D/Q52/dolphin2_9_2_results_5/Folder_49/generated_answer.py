def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 46):
        if s[i:i + 47] == s[i:i + 47][::-1]:
            palindromes.add(s[i:i + 47])
    return palindromes