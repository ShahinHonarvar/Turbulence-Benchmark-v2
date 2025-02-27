def palindrome_of_length_n(string):
    palindromes = set()
    length = len(string)
    for i in range(length - 63):
        substr = string[i:i + 64]
        if substr.lower() == substr.lower()[::-1]:
            palindromes.add(substr)
    return palindromes