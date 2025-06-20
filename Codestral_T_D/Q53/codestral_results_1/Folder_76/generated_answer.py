def palindrome_of_length_at_least_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 137, length + 1):
            substring = string[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes