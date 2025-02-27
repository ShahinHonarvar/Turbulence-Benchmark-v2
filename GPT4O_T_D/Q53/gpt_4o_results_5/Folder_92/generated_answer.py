def palindrome_of_length_at_least_n(s):
    s = ''.join((char for char in s if char.isalpha())).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 10, length + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes