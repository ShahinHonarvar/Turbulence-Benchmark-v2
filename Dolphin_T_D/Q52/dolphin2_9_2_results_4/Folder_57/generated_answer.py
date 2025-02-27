def palindrome_of_length_n(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if set(substring).issubset(alphabet):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes