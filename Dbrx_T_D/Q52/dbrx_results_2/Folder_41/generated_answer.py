def palindrome_of_length_n(string, n=60):
    palindromes = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i + n].lower()
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes