def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 79):
        substr = string[i:i + 80]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes