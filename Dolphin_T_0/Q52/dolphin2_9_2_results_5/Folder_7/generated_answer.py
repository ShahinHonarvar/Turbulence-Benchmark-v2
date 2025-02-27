def palindrome_of_length_n(s):
    s = s.lower()
    num = 416
    palindromes = set()
    for i in range(len(s) - num + 1):
        if s[i:i + num] == s[i:i + num][::-1]:
            palindromes.add(s[i:i + num])
    return palindromes