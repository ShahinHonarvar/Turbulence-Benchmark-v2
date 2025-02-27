def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 137, len(s) + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                set_of_palindromes.add(sub_str)
    return set_of_palindromes