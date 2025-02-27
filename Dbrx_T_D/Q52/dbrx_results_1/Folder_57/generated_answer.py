def palindrome_of_length_n(string, n=92):
    palindromes = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n > len(string) or n < 1:
        return palindromes
    for i in range(len(string) - n + 1):
        if string[i:i + n] == string[i:i + n][::-1]:
            palindromes.add(string[i:i + n])
    return palindromes