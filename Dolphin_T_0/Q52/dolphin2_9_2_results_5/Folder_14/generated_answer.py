def palindrome_of_length_n(s):
    set_of_palindromes = set()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s) - 62):
        sub_s = s[i:i + 63]
        sub_s_lower = ''.join([c.lower() for c in sub_s if c.isalpha()])
        if sub_s_lower == sub_s_lower[::-1]:
            set_of_palindromes.add(sub_s)
    return set_of_palindromes