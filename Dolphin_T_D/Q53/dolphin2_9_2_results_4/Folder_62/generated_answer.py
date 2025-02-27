def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 31, len(string) + 1):
            substring = string[i:j]
            if len(substring) >= 31 and substring != substring[::-1]:
                continue
            else:
                palindromes.add(substring)
    return palindromes