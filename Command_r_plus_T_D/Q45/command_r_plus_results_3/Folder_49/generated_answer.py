def palindromes_between_indices(s):
    sub_str = s[5:8].lower()
    sub_str = ''.join(filter(str.isalpha, sub_str))
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 3, len(sub_str) + 1):
            palindrome = sub_str[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes