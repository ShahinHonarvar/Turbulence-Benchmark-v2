def palindrome_of_length_n(string):
    length = 51
    palindromes = set()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes