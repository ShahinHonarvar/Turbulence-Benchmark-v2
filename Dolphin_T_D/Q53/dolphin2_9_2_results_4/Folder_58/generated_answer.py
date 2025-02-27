def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for length in range(147, 200):
        for i in range(len(string) - length + 1):
            if string[i:i + length] == string[i:i + length][::-1] and string[i:i + length].isalpha():
                palindromes.add(string[i:i + length])
    return palindromes