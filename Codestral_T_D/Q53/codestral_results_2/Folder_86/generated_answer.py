def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 133, len(s) + 1):
            sub_str = s[i:j]
            if sub_str.isalpha() and sub_str.lower() == sub_str[::-1].lower():
                palindromes.add(sub_str)
    return palindromes