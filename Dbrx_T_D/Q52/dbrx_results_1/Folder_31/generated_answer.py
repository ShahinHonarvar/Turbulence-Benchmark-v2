def palindrome_of_length_n(string, n=66):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    if n % 2 == 1:
        half = n // 2
        palindromes = {string[i:half + i + 1] for i in range(len(string) - half) if string[i:half + i + 1] == string[half + i + 1:length + i + 1][::-1]}
    else:
        half = n // 2 - 1
        palindromes = {string[i:half + i + 1] for i in range(len(string) - half) if string[i:half + i + 1] == string[half + i + 2:length + i + 1][::-1]}
    return palindromes