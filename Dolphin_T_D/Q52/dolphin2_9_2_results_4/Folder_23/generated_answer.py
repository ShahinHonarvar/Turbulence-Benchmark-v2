def palindrome_of_length_n(string):
    set_of_palindromes = set()
    for i in range(len(string)):
        for j in range(i + 69, len(string) + 1):
            sub_string = string[i:j]
            lower_sub_string = sub_string.lower()
            if lower_sub_string == lower_sub_string[::-1] and all((letter.isalpha() for letter in lower_sub_string)):
                set_of_palindromes.add(sub_string)
    return set_of_palindromes