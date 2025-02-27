def palindrome_of_length_n(s):
    set_palindromes = set()
    str_lower = s.lower()
    for i in range(len(s) - 86):
        sub_str = str_lower[i:i + 87]
        if sub_str == sub_str[::-1] and sub_str.isalpha():
            set_palindromes.add(sub_str)
    return set_palindromes