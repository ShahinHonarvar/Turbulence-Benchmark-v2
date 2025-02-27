def palindrome_of_length_at_least_n(string, n=53):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = set()
    for i in range(len(string) - n + 1):
        for j in range(i + n, len(string) + 1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes