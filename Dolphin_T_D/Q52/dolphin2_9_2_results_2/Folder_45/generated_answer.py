def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 20):
        if s[i:i + 21] == s[i:i + 21][::-1]:
            palindromes.add(s[i:i + 21])
    return palindromes