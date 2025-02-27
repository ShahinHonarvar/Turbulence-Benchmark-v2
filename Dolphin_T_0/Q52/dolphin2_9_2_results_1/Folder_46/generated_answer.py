def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 463):
        sub = string[i:i + 464]
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes