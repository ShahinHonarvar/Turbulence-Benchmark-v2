def palindrome_of_length_at_least_n(s):
    length_threshold = 44
    palindromes_set = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + length_threshold - 1, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set