def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        if i + 84 <= len(s):
            test_string_1 = s[i:i + 84]
            if test_string_1 == test_string_1[::-1]:
                palindromes.add(test_string_1)
    return palindromes