def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = ''.join((e for e in string if e.isalpha()))
    n = 144
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n - 1, len(string)):
            if string[i:j + 1] == string[i:j + 1][::-1]:
                palindromes.add(string[i:j + 1])
    return palindromes