def palindrome_of_length_n(a_string):
    a_string = a_string.lower()
    set_palindromes = set()
    for i in range(len(a_string)):
        for j in range(i + 85, len(a_string) + 1):
            sub_string = a_string[i:j]
            if sub_string == sub_string[::-1]:
                set_palindromes.add(sub_string)
    return set_palindromes