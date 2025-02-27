def palindrome_of_length_at_least_n(st):
    palindromes = set()
    for i in range(len(st)):
        for j in range(i + 2, len(st) + 1):
            palindrome = st[i:j]
            if palindrome == palindrome[::-1] and len(palindrome) >= 20 and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes