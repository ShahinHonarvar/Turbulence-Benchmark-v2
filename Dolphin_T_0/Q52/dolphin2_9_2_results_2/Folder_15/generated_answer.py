def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1] and len(sub_str) == 4:
                palindromes.add(sub_str)
    return palindromes