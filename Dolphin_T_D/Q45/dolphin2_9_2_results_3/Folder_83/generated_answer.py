def palindromes_between_indices(s):
    sub = s[2:10]
    sub = ''.join([c for c in sub if c.isalpha()])
    sub = sub.lower()
    palindromes = set()
    for length in range(7, len(sub)):
        for i in range(len(sub) - length + 1):
            sub_palindrome = sub[i:i + length]
            if sub_palindrome == sub_palindrome[::-1]:
                palindromes.add(sub_palindrome)
    return palindromes