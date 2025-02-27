def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(64, len(string) + 1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if set(substring).difference(letters) == set() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes