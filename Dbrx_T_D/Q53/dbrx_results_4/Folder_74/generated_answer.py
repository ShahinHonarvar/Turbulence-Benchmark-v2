def is_palindrome(s):
    cp = list(s)
    cp.reverse()
    return ''.join(cp) == s

def length_57_or_more_palindromes(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 56):
        for j in range(i, len(s) - i):
            if j - i + 1 >= 57 and is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes