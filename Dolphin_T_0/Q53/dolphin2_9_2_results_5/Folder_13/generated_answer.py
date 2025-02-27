def palindrome_of_length_at_least_n(string):
    string = ''.join(filter(str.isalpha, string)).lower()
    n = 52
    palindromes = set()
    for i in range(len(string)):
        for length in range(n, len(string) + 1):
            if string[i:i + length] == string[i:i + length][::-1]:
                palindromes.add(string[i:i + length])
    return palindromes