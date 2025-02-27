def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(len(s) - i, 73, -1):
            substring = s[i:i + j].lower()
            if substring == substring[::-1]:
                if substring.strip(string.ascii_letters) == '':
                    if j >= 74:
                        palindromes.add(substring)
    return palindromes