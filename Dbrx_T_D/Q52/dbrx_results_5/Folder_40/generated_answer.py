def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 2):
        if string[i].isalpha() and string[i] == string[i + 2]:
            palindrome = string[i:i + 3].lower()
            if palindrome[0].isalpha():
                palindromes.add(palindrome)
    return palindromes