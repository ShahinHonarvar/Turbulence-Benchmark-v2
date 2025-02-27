def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 28
    string_len = len(string)
    for i in range(string_len):
        for j in range(i + n, string_len + 1):
            substring = string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes