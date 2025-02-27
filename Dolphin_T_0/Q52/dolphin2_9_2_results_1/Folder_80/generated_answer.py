def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        if i + 276 <= len(string):
            sub_string = string[i:i + 276]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes