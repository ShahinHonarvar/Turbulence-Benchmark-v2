def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letter_set = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(string) - 35):
        for j in range(i + 36, len(string) + 1):
            substring = string[i:j]
            if set(substring).issubset(letter_set) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes