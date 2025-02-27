def palindrome_of_length_n(str):
    str = str.lower()
    if len(str) < 24:
        return set()
    palindromes = set()
    for i in range(len(str) - 23):
        for j in range(i + 24):
            palindrome = str[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes