def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(14, len(string) + 1):
        for j in range(0, len(string) - i + 1):
            if string[j:j + i] == string[j:j + i][::-1]:
                palindromes.add(string[j:j + i])
    return palindromes