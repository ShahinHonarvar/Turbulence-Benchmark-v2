def palindromes_of_specific_lengths(s):
    palindrome_set = set()
    for i in range(125, 284):
        for j in range(109, 127):
            if i + j <= len(s):
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    palindrome_set.add(substring)
    return palindrome_set