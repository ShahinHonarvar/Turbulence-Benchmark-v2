def palindrome_of_length_n(string, length=51):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if length % 2 == 0 or length > len(string):
        return set()
    palindromes = set()
    for i in range(len(string) - length + 1):
        if string[i:i + length] == string[i:i + length][::-1]:
            palindromes.add(string[i:i + length])
    return palindromes