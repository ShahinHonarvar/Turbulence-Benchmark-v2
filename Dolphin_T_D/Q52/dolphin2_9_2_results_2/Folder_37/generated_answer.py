def palindrome_of_length_n(s):
    s = s.lower()
    set_palindromes = set()
    for i in range(len(s) - 83):
        sub_s = s[i:i + 84]
        if sub_s == sub_s[::-1]:
            set_palindromes.add(sub_s)
    return set_palindromes