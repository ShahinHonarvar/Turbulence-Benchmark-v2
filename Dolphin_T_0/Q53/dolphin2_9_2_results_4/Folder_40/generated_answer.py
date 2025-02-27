def palindrome_of_length_at_least_n(string):
    string = string.lower()
    set_of_palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 2, length):
            sub_string = string[i:j + 1]
            if sub_string == sub_string[::-1]:
                set_of_palindromes.add(sub_string)
    return set_of_palindromes