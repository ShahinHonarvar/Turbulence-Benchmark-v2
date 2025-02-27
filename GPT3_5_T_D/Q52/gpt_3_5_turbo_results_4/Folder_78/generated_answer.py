def palindrome_of_length_n(string):
    palindromes = set()
    string = ''.join([char for char in string if char.isalpha()])
    for i in range(len(string) - 47):
        substring = string[i:i + 48]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes