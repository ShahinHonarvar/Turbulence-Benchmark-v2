def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 45):
        if string[i:i + 46] == string[i:i + 46][::-1] and string[i:i + 46].isalpha():
            palindromes.add(string[i:i + 46])
    return palindromes