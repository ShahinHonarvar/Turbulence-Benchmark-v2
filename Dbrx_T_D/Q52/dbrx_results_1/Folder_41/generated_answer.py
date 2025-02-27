def palindrome_of_length_n(string):
    string = ''.join((e for e in string if e.isalpha())).lower()
    length = len(string)
    palindromes = set()
    if length < 60:
        return palindromes
    for i in range(length - 60 + 1):
        if string[i:i + 60] == string[i:i + 60][::-1]:
            palindromes.add(string[i:i + 60])
    return palindromes