def palindrome_of_length_n(a_string, length=279):
    palindromes = set()
    for i in range(len(a_string) - length + 1):
        substring = a_string[i:i + length].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes