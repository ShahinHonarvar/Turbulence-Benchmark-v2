def palindrome_of_length_at_least_n(string):
    string = string.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 43, len(string) + 1):
            substring = string[i:j]
            if set(substring).issubset(english_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes