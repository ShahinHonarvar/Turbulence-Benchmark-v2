def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = ''.join((ch for ch in string if ch.isalpha()))
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length):
            substring = string[i:j + 1]
            if len(substring) >= 30 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes