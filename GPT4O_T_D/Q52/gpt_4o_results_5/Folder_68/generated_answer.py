def palindrome_of_length_n(s):
    palindromes = set()
    normalized_string = ''.join(filter(str.isalpha, s)).lower()
    for i in range(len(normalized_string) - 75):
        substring = normalized_string[i:i + 76]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes