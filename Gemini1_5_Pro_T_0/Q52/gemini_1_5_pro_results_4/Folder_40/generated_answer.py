def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 2):
        substring = string[i:i + 3]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring.lower())
    return palindromes