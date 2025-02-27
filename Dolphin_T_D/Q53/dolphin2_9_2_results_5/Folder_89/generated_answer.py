def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 43
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            sub_string = s[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                palindromes.add(sub_string)
    return palindromes