def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 180):
        if s[i:i + 181] == s[i:i + 181][::-1]:
            palindromes.add(s[i:i + 181])
    return palindromes