def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 114):
        for j in range(i + 115, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1] and len(substring) >= 115:
                palindromes.add(substring)
    return palindromes