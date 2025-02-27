from re import findall

def palindrome_of_length_n(string):
    pattern = '[A-Z]'
    filter_string = ''.join([letter for letter in string.upper() if findall(pattern, letter)])
    palindromes = set()
    for i in range(len(filter_string)):
        for j in range(i + 96, len(filter_string) + 1):
            if filter_string[i:j] == filter_string[i:j][::-1]:
                palindromes.add(filter_string[i:j])
    return palindromes