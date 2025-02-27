import string

def palindromes_between_indices(s):
    letters = set(filter(lambda c: c in string.ascii_letters, s))
    sub_str = s[4:10]
    palindromes = set()
    n = len(sub_str)
    for i in range(n):
        for j in range(i + 3, n + 1):
            sub_palindrome = sub_str[i:j]
            if len(sub_palindrome) >= 4 and set(sub_palindrome).issubset(letters) and (sub_palindrome == sub_palindrome[::-1]):
                palindromes.add(sub_palindrome)
    return palindromes