def palindrome_of_length_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s) - 16):
        sub_string = s[i:i + 17]
        if sub_string == sub_string[::-1] and sub_string.isalpha():
            set_of_palindromes.add(sub_string)
    return set_of_palindromes