def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 180):
        sys = string[i:i + 181]
        if sys == sys[::-1]:
            palindromes.add(sys)
    return palindromes