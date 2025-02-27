def palindrome_of_length_n(string):
    n = len(string)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            sub_str = string[i:j + 1]
            if sub_str == sub_str[::-1] and len(sub_str) == 420:
                palindromes.add(sub_str)
    return palindromes