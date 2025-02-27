def palindrome_of_length_at_least_n(a_string):
    a_string = a_string.lower()
    palindromes = set()
    for i in range(len(a_string)):
        for j in range(i + 119, len(a_string) + 1):
            sub_string = a_string[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes