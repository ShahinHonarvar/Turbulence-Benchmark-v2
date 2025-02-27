def palindrome_of_length_at_least_n(s):
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 8, length):
            sub_str = s[i:j + 1]
            if len(sub_str) >= 94 and sub_str.lower() == sub_str[::-1].lower():
                palindromes.add(sub_str)
    return palindromes