def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 15, len(string) + 1):
            substr = string[i:j]
            if len(substr) == 16 and substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes