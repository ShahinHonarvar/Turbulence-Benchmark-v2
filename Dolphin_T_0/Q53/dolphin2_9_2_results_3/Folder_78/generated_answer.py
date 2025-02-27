def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 95, len(string)):
            sub_string = string[i:j + 1]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes