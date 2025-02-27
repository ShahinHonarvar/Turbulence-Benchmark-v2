def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 48
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub_str = s[i:j]
            if sub_str.lower() == sub_str.lower()[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes