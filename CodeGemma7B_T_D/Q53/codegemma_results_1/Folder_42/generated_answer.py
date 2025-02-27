def palindrome_of_length_at_least_n(s):
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1].lower():
                palindrome_set.add(sub_str)
    return palindrome_set