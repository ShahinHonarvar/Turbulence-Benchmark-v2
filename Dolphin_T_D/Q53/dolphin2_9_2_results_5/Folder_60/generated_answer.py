def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 80):
        sub = string[i:i + 80]
        sub = ''.join((e for e in sub if e.isalpha()))
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes