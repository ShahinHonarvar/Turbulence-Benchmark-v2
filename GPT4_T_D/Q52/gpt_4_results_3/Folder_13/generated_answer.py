def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 205):
        sub_str = s[i:i + 206]
        if sub_str == sub_str[::-1] and sub_str.isalpha():
            palindromes.add(sub_str)
    return palindromes