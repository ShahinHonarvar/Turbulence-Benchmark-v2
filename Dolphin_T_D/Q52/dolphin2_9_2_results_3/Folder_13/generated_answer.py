def palindrome_of_length_n(string: str) -> set:
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 206, len(string) + 1):
            substring = string[i:j]
            if substring[::-1] == substring:
                palindromes.add(substring)
    return palindromes