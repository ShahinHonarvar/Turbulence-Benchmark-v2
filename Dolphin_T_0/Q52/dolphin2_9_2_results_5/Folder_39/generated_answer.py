def palindrome_of_length_n(string: str) -> set:
    palindromes = set()
    for index in range(len(string) - 58):
        substring = string[index:index + 59]
        if substring == substring[::-1]:
            palindromes.add(substring.lower())
    return palindromes