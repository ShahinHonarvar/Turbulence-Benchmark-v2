def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 9, len(s)):
            sub_str = s[i:j + 1]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes