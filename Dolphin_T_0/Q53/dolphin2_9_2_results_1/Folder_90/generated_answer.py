def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 139, len(string)):
            sub_string = string[i:j + 1]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes