def palindrome_of_length_n(string):
    set_palindromes = set()
    string = string.lower()
    for char in range(len(string)):
        if char + 69 <= len(string):
            sub_string = string[char:char + 69]
            if sub_string == sub_string[::-1]:
                set_palindromes.add(sub_string)
    return set_palindromes