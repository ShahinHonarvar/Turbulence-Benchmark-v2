def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 96, length):
            sub_str = s[i:j + 1]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes