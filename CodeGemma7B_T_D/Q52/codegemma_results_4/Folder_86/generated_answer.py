def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 180):
        for j in range(i + 181):
            substring = string[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes