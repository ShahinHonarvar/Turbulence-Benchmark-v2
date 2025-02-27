def palindrome_of_length_at_least_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = set()
    for i in range(len(string) - 84):
        for j in range(i, len(string) - i):
            if string[i:j + 1] == string[i:j + 1][::-1]:
                palindromes.add(string[i:j + 1])
    return {p for p in palindromes if len(p) >= 85}